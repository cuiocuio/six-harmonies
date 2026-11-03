# =========================================
# prologue.rpy
# 《Six Harmonies》序章：不完整的前奏
# =========================================

default show_second = False
default is_exiting = False
default first_line_started = False

transform prologue_first_line_fade:
    alpha 0.0
    pause 1.0
    linear 1.5 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

transform prologue_second_line_fade:
    alpha 0.0
    linear 1.5 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

screen dialogue_center():
    modal True

    if not show_second and not is_exiting and not first_line_started:
        timer 1.5 action SetVariable("first_line_started", True)

    # 第一行文字 - 固定在屏幕垂直中心
    showif not is_exiting:
        text "We are not solitary beings adrift in the void of being":
            size 40
            text_align 0.5
            xalign 0.5
            yalign 0.5
            color "#fff"  # 设置为白色文本
            at prologue_first_line_fade

    # 第二行文字 - 固定在第一行下方 40 像素处
    if show_second:
        showif not is_exiting:
            text "but beings-in-relation":
                size 40
                text_align 0.5
                xalign 0.5
                ypos 0.5
                yoffset 40
                color "#fff"  # 设置为白色文本
                at prologue_second_line_fade

    if is_exiting:
        timer 1.8 action Return()

    key "dismiss" action If(is_exiting or (not show_second and not first_line_started), NullAction(), If(not show_second, SetVariable("show_second", True), SetVariable("is_exiting", True)))


label prologue:
    $ show_second = False
    $ is_exiting = False
    $ first_line_started = False
    call screen dialogue_center
    # ---------------------------------
    # 场景一：通知
    # ---------------------------------
    scene bg classroom_day
    with Fade(0.5, 1.0, 0.5)
    play music "bgm/class_noise.mp3"
    pause
    narrator "项目合作课……"
    $ renpy.pause(0.2, hard=True)
    $ class_noise_text = translate_say_menu_text("PPT还停在上一节课的末页{w}，讲台边的音箱没关，发出轻微的噪声")
    narrator "[class_noise_text]"
    $ renpy.pause(0.2, hard=True)
    narrator "正因为是最后一节课，也正因为是快要放学了"
    $ renpy.pause(0.2, hard=True)
    narrator "窗外已经能看到零零散散的学生"
    $ renpy.pause(0.2, hard=True)
    narrator "本来只是很普通的一天"
    $ renpy.pause(0.2, hard=True)
    narrator "普通到我已经点开外卖软件，开始比较哪家盖饭配送更快了"
    $ renpy.pause(0.2, hard=True)
    narrator "直到老师把文件放到讲台上，教室里的杂音才一点点低了下去"
    $ renpy.pause(0.2, hard=True)
    show expression Solid("#0006") as classroom_dim
    with Dissolve(0.3)
    show teacher neutral at left2, chara_enter_left
    with dissolve

    t '"The final comprehensive practice course assignment has been released."'
    $ renpy.pause(0.2, hard=True)
    t '"Starting today, each group will have two weeks to complete a simple but fully functional galgame."'
    $ renpy.pause(0.2, hard=True)
    t '"It must be playable, presentable, and ready for demo day."'
    $ renpy.pause(0.2, hard=True)

    student_a "……啊？"
    $ renpy.pause(0.2, hard=True)
    student_b "等一下，真的要做出来？"
    $ renpy.pause(0.2, hard=True)
    student_c "不是策划案吗？"
    $ renpy.pause(0.2, hard=True)

    t '"Let me be clear."'
    $ renpy.pause(0.2, hard=True)
    t '"Not a proposal. Not slides. Not a prototype mock-up."'
    $ renpy.pause(0.2, hard=True)
    t '"A complete, playable product."'
    $ renpy.pause(0.2, hard=True)

    narrator "教室里先是静了两秒"
    $ renpy.pause(0.2, hard=True)
    narrator "下一秒，就像滚起来的开水一样全炸了"
    $ renpy.pause(0.2, hard=True)

    student_a "两周？这谁做得完啊！"
    $ renpy.pause(0.2, hard=True)
    student_b "我们也没学过什么制作引擎吧！"
    $ renpy.pause(0.2, hard=True)
    student_c "而且还是galgame？！"
    $ renpy.pause(0.2, hard=True)

    t '"Real-world collaboration does not wait for everyone to feel ready."'
    $ renpy.pause(0.2, hard=True)
    t '"You are expected to organize, divide responsibilities, and solve problems as a team."'
    $ renpy.pause(0.2, hard=True)

    narrator "老师转身，在屏幕上切出项目说明"
    $ renpy.pause(0.2, hard=True)
    narrator "黑底白字，简单得过分，也刺眼得过分"
    $ renpy.pause(0.2, hard=True)
    narrator "Two weeks."
    $ renpy.pause(0.2, hard=True)
    narrator "Team project."
    $ renpy.pause(0.2, hard=True)
    narrator "Playable product."
    $ renpy.pause(0.2, hard=True)
    narrator "Demo presentation."
    $ renpy.pause(0.2, hard=True)
    narrator "Group evaluation."
    $ renpy.pause(0.2, hard=True)

    t '"Failure to submit as required will result in the entire group failing this assignment."'
    $ renpy.pause(0.2, hard=True)

    student_a "什么？！"
    $ renpy.pause(0.2, hard=True)
    student_b "全组连坐？！"
    $ renpy.pause(0.2, hard=True)
    student_c "这也太狠了吧——"
    $ renpy.pause(0.2, hard=True)

    narrator "………………"
    $ renpy.pause(0.2, hard=True)
    narrator "只要有人掉链子，全组都要遭殃吗……"
    $ renpy.pause(0.2, hard=True)

    narrator "手机震了一下"
    $ renpy.pause(0.2, hard=True)
    narrator "班级群弹出新消息"
    $ renpy.pause(0.2, hard=True)
    narrator "是分组名单……"
    $ renpy.pause(0.2, hard=True)

    narrator "《综合实践 第七组》"
    $ renpy.pause(0.2, hard=True)
    narrator "Haru"
    $ renpy.pause(0.2, hard=True)
    narrator "Taku"
    $ renpy.pause(0.2, hard=True)
    narrator "Rei"
    $ renpy.pause(0.2, hard=True)
    narrator "Hina"
    $ renpy.pause(0.2, hard=True)
    narrator "Saku"
    $ renpy.pause(0.2, hard=True)
    narrator "Suzu"
    $ renpy.pause(0.2, hard=True)

    narrator "名字都见过"
    $ renpy.pause(0.2, hard=True)
    narrator "但真正说过话的几乎没有……"
    $ renpy.pause(0.2, hard=True)
    narrator "还没来得及把名单看第二遍，老师已经抬眼看了过来"
    t '"Haru."'
    $ renpy.pause(0.2, hard=True)
    show haru troubled at right1, chara_enter_right
    with dissolve
    haru "……是"
    $ renpy.pause(0.2, hard=True)

    t '"You will be the team leader of this group."'
    $ renpy.pause(0.2, hard=True)

    student_b "……哇"
    $ renpy.pause(0.2, hard=True)
    narrator "……………"
    $ renpy.pause(0.2, hard=True)
    scene bg black with Dissolve(0.2)
    $ prologue_transition_text = replace_project_text("{color=#fff}果然{/color}")
    show text "[prologue_transition_text]" with Dissolve(0.3)
    pause
    scene bg classroom_day
    show teacher neutral at left2
    show haru troubled at right1
    with Dissolve(0.5)
    $ renpy.pause(0.2, hard=True)

    t '"You have stable grades, consistent attendance, and you seem dependable."'
    $ renpy.pause(0.2, hard=True)
    t '"So coordination, communication, reporting, and internal follow-up will be your responsibility."'

    show haru ganga 
    haru "老师，我——"
    $ renpy.pause(0.2, hard=True)

    t '"No objections for now."'
    $ renpy.pause(0.2, hard=True)
    t '"If you want to graduate smoothly, lead well."'
    $ renpy.pause(0.2, hard=True)
    show haru sad with Dissolve(0.5)
    narrator "………好的"
    $ renpy.pause(0.2, hard=True)
    scene bg black with Dissolve(0.8)
    centered "{color=#fff}讲台上的投影仍旧亮着，几个关键词像钉子一样钉在那里{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}{b}galgame{/b}{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}{b}two weeks{/b}{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}{b}team leader{/b}{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}……接下来的两周，大概不会安静了{/color}"
    stop music fadeout 0.5
    # ---------------------------------
    # 场景二：第一次集合
    # ---------------------------------
    scene bg black with Dissolve(1.0)
    $ renpy.pause(0.5, hard=True)
    scene bg meeting_room_day with Dissolve(1.5)

    narrator "教学楼一层的讨论室。可移动的圆桌围成圈"
    $ renpy.pause(0.2, hard=True)
    narrator "白墙，玻璃门半开，门外不时有人经过。桌面上散着项目说明、便签纸和几根还没收好的充电线"
    $ renpy.pause(0.2, hard=True)
    narrator "顶灯偏冷，室内安静得能听见翻纸和拖椅子的声音"

    show haru neutral at right2, chara_enter_right
    with dissolve

    narrator "提前到了十分钟"
    $ renpy.pause(0.2, hard=True)
    narrator "总觉得“负责人”这三个字挂在头上之后，会莫名其妙坐不住"
    $ renpy.pause(0.2, hard=True)
    narrator "我把老师发下来的项目说明平铺在桌上，用笔圈出几行最关键的字"
    $ renpy.pause(0.2, hard=True)
    narrator "两周"
    $ renpy.pause(0.2, hard=True)
    narrator "完整可运行"
    $ renpy.pause(0.2, hard=True)
    narrator "现场演示"
    $ renpy.pause(0.2, hard=True)
    narrator "团队合作"
    $ renpy.pause(0.2, hard=True)
    narrator "简单但完整"
    $ renpy.pause(0.2, hard=True)
    narrator "单看都还好"
    $ renpy.pause(0.2, hard=True)
    narrator "并在一起看，有点像威胁……"
    narrator "没等几分钟，门就被推开了。第一个进来的人是……Taku吗"
    show taku neutral at left1, chara_enter_left
    with dissolve
    $ renpy.pause(0.2, hard=True)
    show haru neutral at right2, normal_light
    play music "bgm/happy.mp3" volume 0.15 fadein 0.5
    taku "啊，果然有人已经到了"
    $ renpy.pause(0.2, hard=True)
    taku "你是Haru吧？"
    $ renpy.pause(0.2, hard=True)
    taku "第七组负责人？"

    show haru thinking at right2
    haru "……嗯"
    $ renpy.pause(0.2, hard=True)
    $ class_monitor_intro_text = translate_say_menu_text("这个轻松得像是来参加社团活动的人{w}\n同时也是我的班长")
    narrator "[class_monitor_intro_text]"
    taku "辛苦了啊，第一天就被推上来"
    $ renpy.pause(0.2, hard=True)
    taku "不过说真的，galgame诶"
    $ renpy.pause(0.2, hard=True)
    taku "这题目其实很有意思吧？"
    $ renpy.pause(0.2, hard=True)

    narrator "……有意思在哪"

    show haru neutral at right2
    haru "你看起来挺高兴"
    taku "那当然啊"
    $ renpy.pause(0.2, hard=True)
    show taku neutral with Dissolve(0.3)
    taku "比起做功能演示或者无聊网页，恋爱游戏可是有很多想象空间的"
    $ renpy.pause(0.2, hard=True)
    taku "角色、气氛、对白、分支，只要做得好，很容易让人上头"
    $ renpy.pause(0.2, hard=True)

    narrator "他越说越顺，像脑子里已经有画面了"


    narrator "门又一次被推开，第二个进来的……应该是Rei"
    $ renpy.pause(0.2, hard=True)
    show rei neutral at left2
    with Dissolve(0.3)
    narrator "无神的双眼、黑框眼镜，还有一股已经提前进入工作状态的冷淡气息"
    $ renpy.pause(0.2, hard=True)
    narrator "他扫了一眼房间，就把电脑放稳、开机、连电，动作利落得像是在参加某种技术答辩"
    $ renpy.pause(0.2, hard=True)
    rei "我看过要求了"
    $ renpy.pause(0.2, hard=True)
    taku "这么快就进入正题啊？"
    $ renpy.pause(0.2, hard=True)
    rei "因为这个项目本来就没空绕弯子"
    $ renpy.pause(0.2, hard=True)
    rei "两周要做出来，第一件事就是控规模"
    $ renpy.pause(0.2, hard=True)
    rei "程序部分我来就行"
    $ renpy.pause(0.2, hard=True)
    rei "这种项目，至少别一开始就把自己写死"

    taku "你这话听着好像已经准备砍东西了"

    show rei thinking at left2
    rei "如果不先砍，后面只会死得更难看"
    $ renpy.pause(0.2, hard=True)
    show haru troubled with Dissolve(0.3)
    narrator "两个人第一次对上，气氛就已经有点不对了啊……"

    hide rei with Dissolve(0.8)
    hide taku with Dissolve(0.8)
    show hina neutral at right1 with Dissolve(0.8)

    narrator "第三个进门的是Hina"
    $ renpy.pause(0.2, hard=True)
    narrator "她怀里抱着一本很厚的笔记本，推门时还差点被椅脚绊了一下"
    $ renpy.pause(0.2, hard=True)
    hina "对不起……我是不是来晚了？"
    $ renpy.pause(0.2, hard=True)
    show haru smile at right2, normal_light
    haru "没有，刚开始"
    $ renpy.pause(0.2, hard=True)
    hina "那就好……"
    $ renpy.pause(0.2, hard=True)
    show taku neutral at left1 with Dissolve(0.5)
    taku "让我猜猜，你是写故事的人，对吧？"

    show hina neutral at right1
    hina "……这么明显吗？"
    $ renpy.pause(0.2, hard=True)

    taku "这不是一看就知道嘛"
    $ renpy.pause(0.2, hard=True)
    show hina smile with Dissolve(0.3)
    hina "我……我确实更在意剧情一点"
    $ renpy.pause(0.2, hard=True)
    hina "如果是视觉小说，我希望它读完之后，至少能让人心里留下点什么"
    $ renpy.pause(0.2, hard=True)
    show rei neutral at left2, chara_enter_left with Dissolve(0.5)
    rei "可以"
    $ renpy.pause(0.2, hard=True)
    rei "但你不要写的太散了"
    show hina neutral with Dissolve(0.3)
    hina "嗯，我知道的"
    $ renpy.pause(0.2, hard=True)
    hina "……我不想让我写的故事变成只剩选项和流程的东西"
    $ renpy.pause(0.2, hard=True)
    hina "有些对白，如果刚好落在那个时刻，是会在心里停一下的"
    $ renpy.pause(0.2, hard=True)
    rei "…………"
    $ renpy.pause(0.2, hard=True)
    show haru troubled with Dissolve(0.3)
    narrator "三个人各有各的想法啊……"
    hide hina with Dissolve(0.5)
    hide rei with Dissolve(0.5)   
    hide taku with Dissolve(0.5) 
    narrator "接着进门的……是Saku"
    $ renpy.pause(0.2, hard=True)
    show saku neutral at center, chara_enter_fade
    with Dissolve(0.8)
    
    narrator "白发、冷色调的穿搭、夹在手臂里的绘画本，还有一种明显不想被搭话的气场"
    show haru smile with Dissolve(0.3)
    $ renpy.pause(0.2, hard=True)

    saku "我是负责立绘和UI设计的"
    $ renpy.pause(0.2, hard=True)
    narrator "她坐下以后就没再多说一句，手里的绘画本始终压得很紧，像是不想让任何人看见里面的内容"
    $ renpy.pause(0.2, hard=True)
    show taku excited at left2 with Dissolve(0.3)
    taku "wow，这气质，不愧是搞艺术的"

    $ renpy.pause(0.2, hard=True)
    saku "……"
    $ renpy.pause(0.2, hard=True)

    narrator "她只是瞥了Taku一眼，没有接话"
    hide taku 
    hide saku 
    with Dissolve(0.3)
    show suzu serious at center
    with Dissolve(0.3)
    show haru neutral with Dissolve(0.3)
    narrator "最后进来的是Suzu"
    $ renpy.pause(0.2, hard=True)
    narrator "他戴着半框眼镜，神情严肃，进门时手里就已经夹着整理好的纸页"
    $ renpy.pause(0.2, hard=True)

    suzu "我是Suzu。需求、排期、质量，我来负责"
    $ renpy.pause(0.2, hard=True)
    suzu "这个项目必须尽快定边界。我做了几个方案，等会给你们过目"
    $ renpy.pause(0.2, hard=True)

    narrator "他把纸放到桌上，环视了一圈，像是先完成了一次默默的现场评估"
    $ renpy.pause(0.2, hard=True)    
    show haru smile with Dissolve(0.3)
    haru "嗯嗯，老师说这两周中途可能会抽查，所以今天要先把基础框架定下来"
    $ renpy.pause(0.2, hard=True)
    haru "比如先确定第一周谁负责什么，第二周留多少测试时间之类的……"
    $ renpy.pause(0.2, hard=True)
    suzu "好的，从现在开始，我希望大家尽量别说‘应该来得及’"
    $ renpy.pause(0.2, hard=True)
    suzu "因为如果不做好规划，大概是来不及的"
    $ renpy.pause(0.2, hard=True)
    show rei thinking at left2, chara_enter_left 
    show haru thinking
    with Dissolve(0.5)
    rei "来不及？不可能吧"
    $ renpy.pause(0.2, hard=True)
    rei "这种规模的项目，只要别乱加内容，很快就能搭起来"
    $ renpy.pause(0.2, hard=True)
    suzu "想要做到完美，当然要花很多时间"
    $ renpy.pause(0.2, hard=True)
    suzu "否则我们现在做的一切，最后都只是侥幸"
    $ renpy.pause(0.2, hard=True)
    rei "…………"
    $ renpy.pause(0.2, hard=True)
    taku "哎呀，大家都这么严肃干嘛~"
    $ renpy.pause(0.2, hard=True)
    hide rei
    hide suzu 
    hide haru
    with Dissolve(0.3)
    narrator "……没有人接话"
    $ renpy.pause(0.2, hard=True)
    narrator "整个讨论室的气氛，开始朝着一种不太妙的方向滑过去"
    $ renpy.pause(0.2, hard=True)
    narrator "啪！"
    $ renpy.pause(0.2, hard=True)
    narrator "是绘画本落在地上的声音"
    $ renpy.pause(0.2, hard=True)
    show saku neutral at center 
    with Dissolve(0.3) 
    saku "啧"
    $ renpy.pause(0.2, hard=True)
    show haru thinking at right2 with Dissolve(0.3)
    narrator "……快速撇了一眼绘画本上的内容"
    $ renpy.pause(0.2, hard=True)
    show haru surprised with Dissolve(0.3)
    narrator "咦？"
    $ renpy.pause(0.2, hard=True)
    show haru spark with Dissolve(0.3)
    narrator "哇！"
    $ renpy.pause(0.2, hard=True)
    haru "哇塞，这个画风...如果我没猜错的话，你也喜欢miyako吧"
    scene bg black with Dissolve(0.5)
    centered "{color=#fff}Miyako是我最最喜欢的插画师，我还从来没有遇到过同好呢！{/color}"
    $ renpy.pause(0.5, hard=True)
    $ saku_reaction_text = translate_say_menu_text("{color=#fff}Saku的眼中闪过了一丝....激动？{w}\n但很快，这份激动又消失了{/color}")
    centered "[saku_reaction_text]"
    $ renpy.pause(0.5, hard=True)
    scene bg meeting_room_day with Dissolve(0.5)
    show haru shy at right2
    show saku neutral at center
    haru "啊，我不是说你们的画风雷同"
    $ renpy.pause(0.2, hard=True)
    show haru middleshy with Dissolve(0.3)
    haru "我只是觉得，你们的画给我的感觉很相似.....很独特"
    $ renpy.pause(0.2, hard=True)
    show haru smileshy with Dissolve(0.3)
    haru "我很喜欢这种感觉"
    $ renpy.pause(0.2, hard=True)
    show saku smile with Dissolve(0.3)
    saku "……这样吗，miyako也是我最喜欢的插画师"
    show taku neutral at left2 with Dissolve(0.3)
    taku "哇哦，这个风格，相当的小众呢"
    show suzu neutral at left2 
    hide taku
    with Dissolve(0.3)
    suzu "视觉方面，要多符合一点大众审美，到时候老师还要给我们打分的"
    # ---------------------------------
    # 场景三：坐下之后，问题才真正开始
    # ---------------------------------

    scene bg black with Dissolve(1.0)
    show text ""
    $ renpy.pause(1.5, hard=True)
    scene bg meeting_room_day with Dissolve(1.0)
    show haru troubled at center
    with dissolve
    narrator "六个人终于坐齐了"
    $ renpy.pause(0.2, hard=True)
    narrator "桌上的项目说明、电脑、平板、便签和时间表堆在一起"
    $ renpy.pause(0.2, hard=True)
    narrator "表面上的分工看起来已经很明确了"
    $ renpy.pause(0.2, hard=True)
    narrator "会写、会画、会做程序、会管进度的人都有"
    $ renpy.pause(0.2, hard=True)
    narrator "问题在于，我们看起来……不像是会朝同一个方向走的人"
    $ renpy.pause(0.2, hard=True)
    haru "呃……要不先说说吧"
    $ renpy.pause(0.2, hard=True)
    haru "大家先讲一下，对这个项目的想法和思路？"
    $ renpy.pause(0.2, hard=True)
    stop music fadeout 2.5
    narrator "空气短暂地安静了下来"
    $ renpy.pause(0.2, hard=True)

    narrator "……好尴尬"
    $ renpy.pause(0.2, hard=True)
    narrator "果然我一点也不适合当负责人"

    show taku excited at left2, chara_enter_left
    with dissolve

    taku "你们怎么都不说话"
    $ renpy.pause(0.2, hard=True)
    taku "那我先来"
    $ renpy.pause(0.2, hard=True)
    narrator "……得救了"
    $ renpy.pause(0.2, hard=True)
    narrator "Taku直接起身，拿过桌边的马克笔，在白板上写下几个词"
    $ renpy.pause(0.2, hard=True)
    narrator "角色魅力"
    $ renpy.pause(0.2, hard=True)
    narrator "恋爱感"
    $ renpy.pause(0.2, hard=True)
    narrator "反转"
    $ renpy.pause(0.2, hard=True)
    narrator "分支"
    $ renpy.pause(0.2, hard=True)
    narrator "真结局"
    $ renpy.pause(0.2, hard=True)

    taku "既然是galgame，就别做得太像作业吧？"
    $ renpy.pause(0.2, hard=True)
    taku "至少要有那种让人想继续点下去的感觉。角色得有魅力，剧情得有起伏，最好还能有几条路线，每条路线的氛围都不一样"

    show suzu serious at center, chara_enter_fade
    hide haru
    with dissolve
    play music "bgm/taolun.mp3" fadein 1.5
    suzu "停一下"

    show taku serious at left2 with Dissolve(0.3)
    taku "怎么了？"
    $ renpy.pause(0.2, hard=True)

    suzu "你写的这些东西，任何一项拉大了，都足够把整个项目拖死"
    $ renpy.pause(0.2, hard=True)

    taku "可没有这些，还叫什么恋爱游戏？"
    $ renpy.pause(0.2, hard=True)
    taku "做个只能点下一句、选项还没区别的东西，那不就真成电子作业了？"
    $ renpy.pause(0.2, hard=True)

    suzu "我们的时间很有限"
    $ renpy.pause(0.2, hard=True)
    suzu "要做的是精而完整的作品，不是不切实际地把所有想法都塞进去"
    $ renpy.pause(0.2, hard=True)

    narrator "白板上的字还没写满，两个人已经先撞上了"

    show hina neutral at right2
    with Dissolve(0.3)

    hina "我能理解Taku说的"
    $ renpy.pause(0.2, hard=True)
    hina "如果只是完成任务，那作品可能会很空"

    show rei neutral at left2, chara_enter_left
    hide taku
    with dissolve

    rei "空不空是第二步"
    $ renpy.pause(0.2, hard=True)
    rei "第一步是先让它存在"
    $ renpy.pause(0.2, hard=True)

    hina "可有时候，能不能让人记住，就是差那一点点内容……"
    $ renpy.pause(0.2, hard=True)
    hina "倒不是说一定要写很长……"
    $ renpy.pause(0.2, hard=True)
    $ hina_dialogue_line_text = translate_say_menu_text("只是，人物说出口的话不能只是推进流程{w}\n有些话如果刚好落在那个时刻，会像没说完一样，留在心里")
    hina "[hina_dialogue_line_text]"
    $ renpy.pause(0.2, hard=True)
    show taku neutral at center 
    hide suzu 
    with Dissolve(0.5)

    taku "对啊对啊"
    $ renpy.pause(0.2, hard=True)
    taku "要有余韵啊"
    $ renpy.pause(0.2, hard=True)
    hide rei
    show suzu thinking at left2 
    with dissolve
    suzu "余韵可以有，前提是别变成一堆写不完的分支"
    $ renpy.pause(0.2, hard=True)

    hina "……我也没说一定要很多分支"
    $ renpy.pause(0.2, hard=True)

    narrator "话题没有真正接上，反而越扯越紧"

    
    suzu "视觉方面，最好还是稍微兼顾一点老师的接受度"
    $ renpy.pause(0.2, hard=True)
    suzu "演示打分不是只看作者自己喜不喜欢"
    $ renpy.pause(0.2, hard=True)

    taku "哎，先别管这个"
    $ renpy.pause(0.2, hard=True)
    taku "我还是觉得路线和核心体验要先定，我这边其实已经有几个想法了，比如说——"
    $ renpy.pause(0.2, hard=True)

    narrator "他又开始滔滔不绝"
    $ renpy.pause(0.2, hard=True)
    narrator "Suzu一个接一个地否掉那些超出范围的提案，Hina也忍不住补充自己心里更在意的情感线"
    $ renpy.pause(0.2, hard=True)
    narrator "三个人都没失礼，却谁也不让谁"
    hide taku
    hide hina
    hide suzu with Dissolve(0.5)
    show saku annoyed at left1
    with dissolve
    saku "……我出去透下气"

    hide saku
    with dissolve

    narrator "说完，她便快步走了出去"
    $ renpy.pause(0.2, hard=True)
    narrator "讨论室里短暂安静了一下"
    $ renpy.pause(0.2, hard=True)
    show taku serious at center
    show hina neutral at left2
    with Dissolve(0.5)
    taku "感觉我们的画师好像有点不太好相处啊……"
    $ renpy.pause(0.2, hard=True)
    hina "我……我有点不敢跟她讲话"
    $ renpy.pause(0.2, hard=True)

    narrator "我不知道该怎么回答"
    $ renpy.pause(0.2, hard=True)
    narrator "不过直觉告诉我，Saku并没有表面看起来那么难接近"
    $ renpy.pause(0.2, hard=True)
    show haru troubled at right2
    haru "大家……"
    $ renpy.pause(0.2, hard=True)
    haru "先别讨论这些了"
    $ renpy.pause(0.2, hard=True)
    haru "我想先确认一件事"
    $ renpy.pause(0.2, hard=True)
    haru "我们的首要目标，到底是什么？"
    $ renpy.pause(0.2, hard=True)

    taku "做出让人会心动的galgame"
    $ renpy.pause(0.2, hard=True)

    hina "做出读完以后还有余韵的故事"

    show rei thinking at left2
    hide hina
    with Dissolve(0.5)
    rei "我没什么要求"
    $ renpy.pause(0.2, hard=True)
    rei "能交一个稳定运行的成品就行"
    $ renpy.pause(0.2, hard=True)

    narrator "Suzu推了推眼镜，手指点在桌上的计划表上"
    $ renpy.pause(0.2, hard=True)

    suzu "已经四个答案了"
    $ renpy.pause(0.2, hard=True)
    suzu "这就是现在最大的问题"

    # ---------------------------------
    # 场景四：沉默与转折
    # ---------------------------------
    scene bg black with Dissolve(1.5)
    $ renpy.pause(1.0, hard=True)
    scene bg meeting_room_evening with Dissolve(1.5)

    $ renpy.pause(0.8, hard=True)
    narrator "窗外的天色慢慢暗下来"
    $ renpy.pause(0.2, hard=True)
    narrator "讨论室里的白灯有点冷，落在桌上的纸面上，所有字都显得过分清楚"
    $ renpy.pause(0.2, hard=True)
    narrator "倒不是因为谁说服了谁，房间才安静下来"
    $ renpy.pause(0.2, hard=True)
    narrator "恰恰相反"
    $ renpy.pause(0.2, hard=True)
    narrator "因为每个人都说得通，所以谁也不想先退"
    $ renpy.pause(0.2, hard=True)
    show taku neutral at left1, chara_enter_left with Dissolve(0.5)
    narrator "Taku想让它热闹、浪漫、值得反复点开"
    $ renpy.pause(0.2, hard=True)
    show rei neutral at left2, chara_enter_left with Dissolve(0.5)
    narrator "Rei只关心代码结构和最终能不能稳定运行"
    $ renpy.pause(0.2, hard=True)
    show hina neutral at right1, chara_enter_right with Dissolve(0.5)
    narrator "Hina想给这个游戏留下一点情感上的重量"
    $ renpy.pause(0.2, hard=True)
    show suzu serious at right2, chara_enter_fade with Dissolve(0.5) 
    narrator "Suzu考虑的，已经是第一周结束前必须完成哪些部分"
    $ renpy.pause(0.2, hard=True)
    hide taku
    hide rei
    hide suzu
    hide hina
    with Dissolve(0.5)
    pause 0.5
    show saku neutral at center, chara_enter_fade with Dissolve(0.5) 
    narrator "Saku的想法……此刻谁也说不准"
    $ renpy.pause(0.2, hard=True)
    hide saku
    show haru bunaifan
    with Dissolve(0.5)
    narrator "………………"
    $ renpy.pause(0.2, hard=True)
    show haru neutral with Dissolve(0.3)
    stop music fadeout 1.0
    scene bg black with Dissolve(0.8)
    centered "{color=#fff}我的目光落回项目说明第一页{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}老师写在最上面的那句话，又一次撞进眼里{/color}"
    $ renpy.pause(0.5, hard=True)
    centered '{color=#fff}"Please focus on team collaboration to create a simple yet complete visual novel."{/color}'
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}简单{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}完整{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}团队合作{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}听上去很像套话……{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}但不得不说，确实挺有道理{/color}"
    $ renpy.pause(0.5, hard=True)
    scene bg meeting_room_evening with Dissolve(0.8)

    # ---------------------------------
    # 场景五：Haru第一次作出决定
    # ---------------------------------
    show haru thinking with Dissolve(0.3)
    narrator "………………"
    $ renpy.pause(0.2, hard=True)
    narrator "我明白了……"
    $ renpy.pause(0.2, hard=True)
    show haru smile with Dissolve(0.3)
    haru "各位，先停一下"
    $ renpy.pause(0.2, hard=True)
    haru "我有些话想说"
    $ renpy.pause(0.2, hard=True)
    narrator "四个人都看向了我"
    $ renpy.pause(0.2, hard=True)
    scene bg black with Dissolve(0.8)
    play music "bgm/jihua.mp3" fadein 5.0 volume 0.3
    centered "{color=#fff}白板上还留着刚才写下来的词{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}角色魅力{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}分支{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}余韵{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}视觉统一{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}稳定运行{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}时间控制{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}每一项都像正确答案的一部分{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}可如果一开始就全抓，最后多半什么也抓不住吧{/color}"
    $ renpy.pause(0.2, hard=True)
    centered "{color=#fff}其实……{/color}"
    $ renpy.pause(0.2, hard=True)
    scene bg meeting_room_evening with Dissolve(0.8)
    show haru smile with Dissolve(0.3)
    haru "其实我们现在不是没想法"
    $ renpy.pause(0.2, hard=True)
    haru "是每个人都有想做的东西，而且都觉得自己的那一块不能少"
    $ renpy.pause(0.2, hard=True)
    show taku neutral at left2 with Dissolve(0.3)
    taku "这不很正常吗？"
    $ renpy.pause(0.2, hard=True)

    haru "正常"
    $ renpy.pause(0.2, hard=True)
    haru "但如果我们再这样聊下去，今天可能什么都定不下来"
    $ renpy.pause(0.2, hard=True)
    show haru smile with Dissolve(0.3)
    narrator "Taku没再接话"
    $ renpy.pause(0.2, hard=True)
    show suzu neutral at left2
    hide taku
    with Dissolve(0.3)
    narrator "Suzu也只是看着我，像是在等我到底准备站哪一边"
    $ renpy.pause(0.2, hard=True)
    hide suzu with Dissolve(0.3)
    haru "我觉得先把框架立住"
    $ renpy.pause(0.2, hard=True)
    $ framework_outline_text = translate_say_menu_text("先把主题和主线大纲定下来，不用太宏大{w}，也不要太复杂")
    haru "[framework_outline_text]"
    $ renpy.pause(0.2, hard=True)
    scene bg black with Dissolve(0.8)
    $ quiet_room_text = translate_say_menu_text("{color=#fff}房间里很安静……{w}\n大家都在很认真地听我讲话……{/color}")
    centered "[quiet_room_text]"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}其实每个人都只是想要尽一份力而已{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}然后就是——{/color}"
    $ renpy.pause(0.5, hard=True)
    scene bg meeting_room_evening with Dissolve(0.8)
    show haru smile with Dissolve(0.3)
    haru "在时间真的允许之前，先别碰多路线、隐藏结局、额外玩法这些会把工作量一下子撑大的东西"
    $ renpy.pause(0.2, hard=True)
    haru "把主线和核心体验做稳，比什么都重要"
    show haru proud with Dissolve(0.3)
    $ renpy.pause(0.2, hard=True)
    $ haru_confirmation_text = translate_say_menu_text("嗯……{w}对，就这样……")
    haru "[haru_confirmation_text]"


    show suzu serious at center, normal_light
    hide haru
    with Dissolve(0.3)
    suzu "如果是这样，我今晚就能排出第一版进度"

    show rei thinking at left2, normal_light with Dissolve(0.3)
    rei "我同意"
    $ renpy.pause(0.2, hard=True)
    rei "先做能完成的基本盘"

    show hina smile at right2, normal_light with Dissolve(0.3)
    hina "这样的话，剧情也可以先集中写一条真正成立的主线"
    $ renpy.pause(0.2, hard=True)
    hina "至少不会一开始就散掉"

    show taku neutral at center, normal_light
    show haru smile at right2
    hide suzu
    hide hina
    with Dissolve(0.3)
    taku "也就是说，现在先别想多路线和真结局？"
    $ renpy.pause(0.2, hard=True)

    haru "先别想太远"
    $ renpy.pause(0.2, hard=True)
    haru "先让它成为一个完整的作品"
    $ renpy.pause(0.2, hard=True)

    taku "……听起来很保守"
    $ renpy.pause(0.2, hard=True)
    show haru smile at right2
    hide hina
    with Dissolve(0.3)
    haru "或许是这样"
    $ renpy.pause(0.2, hard=True)
    haru "但我们现在最需要的，大概就是保守一点的起点"
    $ renpy.pause(0.2, hard=True)
    stop music fadeout 6.0
    # ---------------------------------
    # 场景六：暂时成形的团队
    # ---------------------------------
    taku "那我呢？"
    $ renpy.pause(0.2, hard=True)
    taku "总不能让我负责被打击积极性吧？"
    $ renpy.pause(0.2, hard=True)
    haru "你就负责把‘有意思’这件事留下来吧"
    $ renpy.pause(0.2, hard=True)
    haru "但前提是，别把它一下扩成十条路线"
    $ renpy.pause(0.2, hard=True)
    taku "……行"
    $ renpy.pause(0.2, hard=True)
    taku "先忍一手"
    $ renpy.pause(0.2, hard=True)
    show suzu neutral at left2
    hide rei
    with Dissolve(0.3)
    suzu "那我先记一下暂定原则"
    $ renpy.pause(0.2, hard=True)
    suzu "第一，范围缩小。第二，优先主线。第三，先完成核心演示版本，再考虑追加内容"
    $ renpy.pause(0.2, hard=True)
    show rei neutral at center 
    hide taku
    with Dissolve(0.3)
    rei "程序这边，我最好在明晚前拿到初步结构"
    $ renpy.pause(0.2, hard=True)
    show hina smile at left2 
    hide suzu
    with Dissolve(0.3)
    hina "我今晚整理一下主线大纲"
    $ renpy.pause(0.2, hard=True)
    hina "如果只做一条主线，我会先把角色关系压清楚"
    $ renpy.pause(0.2, hard=True)

    scene bg black with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    play music "bgm/waltz.mp3" 
    centered "{color=#fff}……这不算达成一致{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}最多只能算是大家终于承认了眼下必须先从同一个起点出发{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}……直到会议快结束，Saku也没有再回来……{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}……刚刚压下去的不安，又在心里慢慢浮了上来{/color}"

    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}………………{/color}"
    centered "{color=#fff}计划没有在今天就变得很完美{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}我们也没有因为这一场谈话，就忽然理解彼此、信任彼此，或者默契到像认识很久一样{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}其实我们还不熟{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}还不知道这个开局就意见四散的六人小组，到底能不能做出一部真正属于我们的游戏{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}不过，有一件事，已经和之前不一样了{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}这不再只是老师扔下来的麻烦任务{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}也不再只是群聊里一张随手发出的名单{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}这是我们六个人共同要面对的东西{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}也许很乱{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}也许很难{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}也许从第一步开始就不算顺利{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}但前奏这种东西{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}本来一开始就很少完整{/color}"
    $ renpy.pause(1.5, hard=True)
    $ prologue_end_card_text = replace_project_text("{size=72}{color=#fff}{b}《Six Harmonies》{/b}{/color}{/size}\n{size=46}{color=#fff}{b}序章：不完整的前奏{/b}{/color}{/size}")
    show text "[prologue_end_card_text]" at truecenter
    with Dissolve(5.5)
    pause
    stop music fadeout 1.5
    scene bg black
    with fade
    pause
    return
