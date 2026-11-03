init -100 python:
    ENGLISH_SAY_MENU_TEXT = globals().get("ENGLISH_SAY_MENU_TEXT", {})
    ENGLISH_DISPLAY_TEXT = globals().get("ENGLISH_DISPLAY_TEXT", {})

    _previous_say_menu_text_filter = config.say_menu_text_filter
    _previous_replace_text = config.replace_text

    def normalize_language_pref(language):
        return "english" if language == "english" else None

    def has_language_pref():
        return hasattr(persistent, "language_pref")

    def get_language_pref():
        return normalize_language_pref(getattr(persistent, "language_pref", None))

    def set_language_pref(language):
        persistent.language_pref = normalize_language_pref(language)
        renpy.save_persistent()

    def is_language_selected(language):
        return get_language_pref() == normalize_language_pref(language)

    def apply_saved_language():
        renpy.change_language(get_language_pref())

    def translate_say_menu_text(text):
        if _previous_say_menu_text_filter is not None:
            text = _previous_say_menu_text_filter(text)

        if get_language_pref() == "english":
            return ENGLISH_SAY_MENU_TEXT.get(text, text)

        return text

    def replace_project_text(text):
        if _previous_replace_text is not None:
            text = _previous_replace_text(text)

        if get_language_pref() == "english":
            return ENGLISH_DISPLAY_TEXT.get(text, text)

        return text

    def timed_choice_timer_label(remaining):
        if get_language_pref() == "english":
            return "Time Left: {}s".format(remaining)

        return "剩余时间：{} 秒".format(remaining)

    config.say_menu_text_filter = translate_say_menu_text
    config.replace_text = replace_project_text


screen language_switch_buttons():
    hbox:
        style_prefix "language_switch"
        spacing 12

        textbutton "中文":
            action [Function(set_language_pref, None), Language(None)]
            selected is_language_selected(None)

        textbutton "English":
            action [Function(set_language_pref, "english"), Language("english")]
            selected is_language_selected("english")


screen language_select():
    modal True
    zorder 250

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 48
        ypadding 40

        vbox:
            spacing 20
            xalign 0.5

            text "语言 / Language":
                style "language_select_title"
                xalign 0.5
                text_align 0.5

            text "请选择游戏语言\nChoose your game language":
                style "language_select_prompt"
                xalign 0.5
                text_align 0.5

            hbox:
                style_prefix "language_switch"
                spacing 18
                xalign 0.5

                textbutton "中文":
                    action [Function(set_language_pref, None), Language(None), Return()]
                    selected is_language_selected(None)

                textbutton "English":
                    action [Function(set_language_pref, "english"), Language("english"), Return()]
                    selected is_language_selected("english")


label before_main_menu:
    if has_language_pref():
        $ persistent.language_pref = get_language_pref()
        $ renpy.save_persistent()
        $ apply_saved_language()
    else:
        call screen language_select

    return


style language_switch_button is gui_button
style language_switch_button_text is gui_button_text
style language_switch_label is gui_text
style language_select_title is gui_label_text
style language_select_prompt is gui_text

style language_switch_button:
    xpadding 18
    ypadding 10
    background Solid("#ffffff18")

style language_switch_label:
    size 24
    color "#f2f2f2"

style language_switch_button_text:
    color "#f8fbff"
    hover_color "#ffd7e5"
    selected_color "#ffffff"
    outlines [(2, "#24384d99", 0, 0)]

style language_select_title:
    size 42

style language_select_prompt:
    size 28
    color "#f2f2f2"
