module Tags.View exposing (..)

import Types exposing (..)
import State exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput, onClick, onCheck)


view : Model -> Html Msg
view model =
    div [ class "overflow-hidden ph4 ph3-m ph3-l mt5" ]
        [ div [ class "tl w-60-ns center" ] [ h3 [] [ text "Personalise your results:" ] ]
        , div [ class ("tag-container w-200-ns w-330 relative center " ++ (getPosition model.position)) ]
            [ render_filter_block model 1 model.issue_label model.issue_tags ("mr-1p-ns mr-5 " ++ (get_active model 1))
            , render_filter_block model 2 model.reason_label model.reason_tags ("mr-1p-ns mr-5 " ++ (get_active model 2))
            , render_filter_block model 3 model.content_label model.content_tags (get_active model 3)
            ]
        ]


render_filter_block : Model -> Int -> String -> List String -> String -> Html Msg
render_filter_block model num filter_label tags classname =
    div
        [ class
            ("tag-card br1 shadow-2 w-30 tl pa4-ns pa3 mb3 dib h6 v-mid relative "
                ++ classname
                ++ if not (is_active model num) then
                    " pointer"
                   else
                    ""
            )
        , onClick
            (if (is_active model num) then
                NoOp
             else
                (ChangePosition num)
            )
        ]
        ([ h3 [ class "ma0" ] [ text ("Q" ++ (toString num) ++ " of 3") ]
         , h4 [ class "w-70 mv3" ] [ text filter_label ]
         ]
            ++ [ div [ class "pv2 overflow-scroll h4" ] ([] ++ (List.map (\t -> render_tag_list t model.selected_tags num) tags)) ]
            ++ [ div [ class "mt3 absolute bottom-1 w-100 ph4-ns ph1 left-0" ]
                    [ div [ class "w-50 dib tl" ]
                        [ previous_button num ]
                    , div [ class "w-50 dib tr" ]
                        [ next_button num ]
                    ]
               ]
        )


render_tag_list : String -> List Tag -> Int -> Html Msg
render_tag_list tag selected_tags num =
    div [ class "dib" ]
        [ button
            [ class ("b--lm-orange ba br2 ph2 pv1 lh-tag dib mb1 pointer font nunito mr1 " ++ (getTagColour (create_tag num tag) selected_tags))
            , onClick (SelectTag (create_tag num tag))
            ]
            [ text tag ]
        ]


getPosition : Int -> String
getPosition pos =
    case pos of
        1 ->
            "l-12-ns r-0"

        2 ->
            "r-50-ns r-115"

        3 ->
            "r-112-ns r-230"

        _ ->
            "l-12-ns"


getTagColour : Tag -> List Tag -> String
getTagColour tag selected_tags =
    if List.member tag selected_tags then
        "lm-bg-orange-70"
    else
        "lm-bg-orange-20"


create_tag : Int -> String -> Tag
create_tag num name =
    case num of
        1 ->
            Tag "issue" name

        2 ->
            Tag "reason" name

        3 ->
            Tag "content" name

        _ ->
            Tag "issue" name


is_active : Model -> Int -> Bool
is_active model pos =
    model.position == pos


get_active : Model -> Int -> String
get_active model pos =
    if (is_active model pos) then
        ""
    else
        "inactive"


previous_button : Int -> Html Msg
previous_button pos =
    case pos of
        1 ->
            text ""

        _ ->
            button
                [ class "tl dib bn bg-white pointer"
                , onClick (ChangePosition (pos - 1))
                ]
                [ div [ class "h2 br-100 w2 ba bw2 b--lm-dark-blue lm-orange pa1 mr2 dib" ] [ text "◀" ]
                , div [ class "dib nunito-bold w-50 w-auto-ns" ] [ text "previous question" ]
                ]


next_button : Int -> Html Msg
next_button pos =
    case pos of
        3 ->
            button [ class "f5 link dib ph3 pv2 br1 pointer nunito tracked inner-shadow-active lm-white lm-bg-dark-blue button lm-bg-orange-hover lm-dark-blue-hover" ] [ a [ class "link", href "#results" ] [ text "Search" ] ]

        _ ->
            button
                [ class "tr dib bn bg-white pointer"
                , onClick (ChangePosition (pos + 1))
                ]
                [ div [ class "dib nunito-bold w-50 w-auto-ns" ] [ text "next question" ]
                , div [ class "h2 br-100 w2 ba bw2 b--lm-dark-blue lm-orange pa1 ml2 dib" ] [ text "▶" ]
                ]
