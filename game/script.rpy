# =========================================
# script.rpy
# 《Six Harmonies》主脚本文件
# =========================================

## 游戏初始化后开始的标签
default team_cohesion_score = 0
default ending_type = "good"

label show_chapter_end_card(chapter_number, chapter_title):
    window hide
    scene bg black
    with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    $ chapter_end_card_text = replace_project_text("{size=72}{color=#fff}{b}%s{/b}{/color}{/size}\n{size=46}{color=#fff}{b}%s{/b}{/color}{/size}" % (chapter_number, chapter_title))
    show text "[chapter_end_card_text]" as chapter_end_card at truecenter
    with Dissolve(5.5)
    pause
    hide chapter_end_card
    with Dissolve(0.5)
    return

label start:
    $ team_cohesion_score = 0
    $ ending_type = "good"
    ## 开始序章
    call prologue from _call_prologue
    
    ## 序章结束后进入第一章
    call chapter_1 from _call_chapter_1

    ## 第一章结束后进入第二章
    call chapter_2 from _call_chapter_2

    ## 第二章结束后进入第三章
    call chapter_3 from _call_chapter_3

    ## 第三章结束后进入第四章
    call chapter_4 from _call_chapter_4

    ## 第四章结束后，先返回标题菜单
    return
