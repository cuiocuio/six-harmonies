# =========================================
# chapter4.rpy
# Six Harmonies Chapter 4: The Last Days Pass Like Summer
# =========================================

label chapter_4:

    scene bg black
    with Fade(0.5, 0.8, 0.5)
    scene bg meeting_room_day
    with Dissolve(1.0)
    play music "bgm/newpath.mp3" volume 0.5 fadein 0.5
    show haru neutral at center, chara_enter_fade
    with dissolve
    narrator "下午，讨论室的门被我推开的时候，里面已经坐了几个人。"
    narrator "空调开着，桌上摊着电脑、平板、打印稿，还有几杯刚买回来的水。"
    narrator "窗外天还很亮，玻璃上映着一点浅浅的反光，整个房间看起来和平时没什么两样。"
    narrator "……可我还是在门口停了半秒。"
    narrator "因为这种“和平时没什么两样”，本身就已经很难得了。"
    narrator "前几天那场闹得所有人都不太好受的争执过去以后，气氛总算一点点缓了回来。"
    narrator "不是谁都假装没发生过。"
    narrator "而是大家都默契地往后退了一步，没再去碰那些会让人一下子僵住的话题。"
    show taku neutral at left2, chara_enter_left
    show hina neutral at right2, chara_enter_right
    hide hina
    show suzu serious at right2, chara_enter_right
    with dissolve
    haru "那个，我有个提议。"
    narrator "几个人都抬头看我。"
    narrator "Suzu正低头看时间表，闻言也把笔放了下来。Hina抱着笔记本，眼神很认真。Taku原本还在拆零食袋子，动作一下子顿住了。"
    haru "反正也没几天了。"
    haru "要不这段时间，大家只要没课，就尽量来会议室一起工作吧。"
    haru "不是说一定要一直讨论。"
    haru "就是……各做各的也行，但都待在一起的话，有什么问题能直接说，效率应该会高很多。"
    narrator "说完以后，我自己都有点心虚。"
    narrator "总觉得这种提议，听起来很像是把大家的命又往 deadline 那边推了一把。"
    suzu "可以。"
    suzu "这样确实会比较方便。"
    hide taku
    show rei neutral at left2, chara_enter_left
    with dissolve
    rei "我没意见。"
    rei "反正程序有问题，你们本来就得随时找我。"
    hide suzu
    show hina shy at right2, chara_enter_right
    hina "我也可以。"
    hina "大家都在的话，改东西的时候也比较安心。"
    hide rei
    show taku excited at left2
    taku "哇。"
    taku "这是什么，最终决战前的集体驻扎模式？"
    show haru troubled at center
    haru "……怎么说得跟热血战斗番一样。"
    taku "谁说我不愿意了。"
    taku "我举双手双脚赞成。"
    taku "这种“大家一起并肩熬到最后”的桥段，我超喜欢的好吗。"
    narrator "虽然他还是很吵。"
    narrator "但不知道为什么，被他这么一搅，原本还有点正经的气氛反而松下来了。"
    hide rei
    with dissolve
    narrator "于是，从这天下午开始，讨论室就真的慢慢变成了我们的临时据点。"
    narrator "傍晚前，人差不多都到齐了。"
    narrator "桌面被各种东西堆得比平时更满，连插线板都快不够用了。"
    narrator "Hina把剧本和笔记本整整齐齐摆在一起，Suzu旁边则是那叠被改了不知道多少次的资料。"
    narrator "而 Taku——带来了一大袋零食。"
    haru "你怎么还真把这儿当驻扎点了。"
    show taku excited at left2
    taku "那当然。"
    taku "高强度脑力劳动的前提是什么？"
    taku "是糖分，是快乐，是薯片。"
    hide taku
    show rei neutral at left2, chara_enter_left
    with dissolve
    rei "纯属你自己想吃吧。"
    hide rei
    show taku annoyed at left2
    taku "你不用这么直接吧。"
    hide rei
    hide taku
    show saku neutral at left2, chara_enter_left
    with dissolve
    narrator "Hina低头笑了一下。"
    narrator "Saku伸手拿了一包小饼干，动作很自然。"
    narrator "Suzu看了一眼那袋零食，像是想说什么，最后也只是叹了口气。"
    hide saku
    show taku excited at left2
    taku "来吧各位。"
    taku "第七组临时基地，今天正式开始运作。"
    haru "这个名字为什么听起来越来越像非法组织了。"
    taku "你不懂，这叫仪式感。"
    hide taku
    show rei neutral at left2, chara_enter_left
    with dissolve
    rei "你先做到“少说十句废话”再说。"
    narrator "我坐下来，忍不住笑了一下。"
    narrator "光是看到他们像平时那样拌嘴，我心里那点一直没完全放下的东西，也终于慢慢落了地。"
    hide rei
    hide saku
    with dissolve
    scene bg meeting_room_evening
    with Dissolve(1.0)
    show rei serious at center, chara_enter_fade
    with dissolve
    narrator "晚上，窗外已经彻底暗了下来。"
    narrator "房间里只剩下翻纸、敲键盘和偶尔说几句话的声音。"
    narrator "突然，Rei那边忽然停了。"
    narrator "他盯着屏幕看了几秒，手指在键盘上敲下最后几下，然后很轻地“咔”一声，按了回车。"
    rei "……好了。"
    show taku excited at left2, chara_enter_left
    show haru surprised at right2, chara_enter_right
    with dissolve
    narrator "桌边其他几个人同时抬起了头。"
    narrator "Taku反应最快，整个人几乎是一下子从椅子上弹起来的。"
    taku "什么好了？！"
    rei "最初可运行版本。"
    hide haru
    show hina smile at right2, chara_enter_right
    with dissolve
    narrator "房间安静了半秒。"
    narrator "下一秒，所有人都围了过去。"
    hide taku
    show haru surprised at left2, chara_enter_left
    haru "真的假的……"
    hina "已经可以跑了吗？"
    hide taku
    hide haru
    show saku smile at left2, chara_enter_left
    with dissolve
    saku "这么快。"
    hide hina
    show suzu serious at right2, chara_enter_right
    with dissolve
    suzu "基础功能都接好了？"
    rei "最基础的可以了。"
    narrator "我们几个围在电脑前，甚至连椅子都顾不上搬。"
    narrator "鼠标点下去的时候，我莫名其妙跟着屏住了呼吸。"
    narrator "下一秒，窗口弹了出来。"
    with None
    scene bg black
    with Dissolve(0.8)
    centered "{color=#fff}标题界面、背景、对话框、按钮、音乐。{/color}"
    $ renpy.pause(0.4, hard=True)
    centered "{color=#fff}那些原本散在每个人手里的东西，终于在同一个画面里连起来了。{/color}"
    $ renpy.pause(0.4, hard=True)
    centered "{color=#fff}直到这一刻，我才第一次真正意识到。{/color}"
    $ renpy.pause(0.4, hard=True)
    centered "{color=#fff}我们不是在“准备做一款游戏”。{/color}"
    $ renpy.pause(0.4, hard=True)
    centered "{color=#fff}我们是在“真的把它做出来了”。{/color}"
    $ renpy.pause(0.6, hard=True)
    scene bg meeting_room_evening
    with Dissolve(0.8)
    show haru neutral at left2, chara_enter_left
    hide haru
    show taku excited at left2, chara_enter_left
    show rei serious at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    hide saku
    show suzu serious at right2, chara_enter_right
    with dissolve
    narrator "游戏正式开始以后，大家都下意识安静了一点。"
    narrator "开头的背景慢慢切进来，文字一行行跳出来，角色立绘也按顺序出现在画面里。"
    narrator "明明这些东西每个人都已经看过很多次了，可真正变成“游戏”的样子时，感觉却完全不一样。"
    narrator "像是那些原本还散着的东西，终于长成了一个完整的样子。"
    narrator "又像是，我们这段时间熬出来的那些夜、改过的那些对白、争来争去的那些细节，全都被装进了这个窗口里。"
    taku "这个BGM神了，太有感觉了。"
    hide saku
    hide suzu
    show hina smile at right2, chara_enter_right
    with dissolve
    hina "这句台词原来放在这里会这么合适……"
    hide hina
    show saku neutral at right2, chara_enter_right
    with dissolve
    saku "立绘位置可以再微调一点。"
    hide saku
    show suzu serious at right2, chara_enter_right
    suzu "文字速度后面再试试要不要调慢点。"
    rei "没问题。"
    narrator "大家一边玩一边聊着。"
    narrator "那种感觉挺奇妙的，像围着什么刚刚煮好的东西，一边尝一边认真讨论味道怎么样。"
    narrator "突然，画面切换的一瞬间，屏幕上的立绘“唰”地一下放大了好几倍。"
    narrator "原本好好站在一侧的人，直接怼满了半个屏幕，脸近得仿佛下一秒就要从电脑里冲出来。"
    hide taku
    show haru surprised at left2
    haru "——等一下？！"
    hide saku
    hide suzu
    show hina speechless at right2, chara_enter_right
    with dissolve
    hina "哇！怎么回事？"
    hide haru
    show taku excited at left2
    taku "这是登场还是袭击啊？！"
    hide hina
    show saku serious at right2, chara_enter_right
    with dissolve
    saku "……好有压迫感。"
    narrator "整个房间安静了不到半秒，下一秒就全笑了。"
    narrator "本来还挺正常的一句日常对白，配上这张突然超近距离贴脸的立绘，效果瞬间从校园AVG变成了某种奇怪的喜剧现场。"
    rei "……啊，我比例参数写错了。"
    hide saku
    show suzu serious at right2, chara_enter_right
    suzu "先记一下。"
    taku "不是，你咋忍住不笑的。"
    narrator "然而事情显然还没完。"
    narrator "下一段本来应该切到教室背景，结果背景没换成功，角色就这么站在图书馆里说出了“那我们回教室吧”。"
    hide taku
    show haru smile at left2
    haru "时空错乱了啊喂！"
    hide haru
    show taku excited at left2
    taku "这是瞬移失败了吧哈哈哈！"
    rei "这个也记下。"
    narrator "后面还有文字框一闪一闪不肯消失、选项按钮突然偏到角落里、BGM慢半拍进来的问题。"
    narrator "不过谁都没觉得烦。"
    narrator "每冒出一个小 bug，大家都会先笑一轮，然后再很认真地把它记下来。"
    narrator "这真的就是我们做出来的东西。"
    narrator "它就在这里。"
    narrator "亮着，响着，会切背景，也会突然把立绘放大到吓人一跳。"
    narrator "……它确实活起来了。"
    hide haru
    hide taku
    hide rei
    hide saku
    hide suzu
    with dissolve
    with None
    scene bg black
    with Dissolve(0.8)
    stop music fadeout 5.0
    scene bg dorm_room_day
    with Dissolve(0.8)
    show haru neutral at center, chara_enter_fade
    with dissolve
    narrator "第二天上午，宿舍里安安静静的，窗外阳光很好。"
    narrator "我躺在椅子上刷了会儿手机，突然想起来，今天大家好像都没什么课。"
    narrator "最近这段时间，我们不是在教学楼，就是在讨论室。"
    narrator "连吃饭和回宿舍都像是顺便。"
    narrator "虽然效率是上去了，但总觉得，大家都被闷得有点久了。"
    narrator "而且现在这种气氛，好不容易重新变回舒服的样子。"
    narrator "我也有点想趁这个机会，让大家再轻松一点。"
    haru "今天大家好像都没什么课诶。"
    haru "要不要一起去沙湖公园走走？"
    narrator "消息发出去没多久，群里就有了动静。"
    show taku excited at left2
    play music "bgm/KAROYAKAGirls.mp3" volume 0.25 loop fadein 1.0
    taku "我要去！"
    show hina smile at right2, chara_enter_right
    hina "我也想去。"
    hide taku
    show rei neutral at left2, chara_enter_left
    rei "可以。"
    hide hina
    show suzu serious at right2, chara_enter_right
    suzu "我没意见。"
    hide rei
    show saku neutral at left2, chara_enter_left
    saku "嗯。"
    narrator "……居然全票通过了。"
    hide haru
    with dissolve
    scene bg shahu_park_lakeside_day
    with Dissolve(1.0)
    show taku neutral at left2, chara_enter_left
    hide taku
    show haru neutral at left2, chara_enter_left
    show hina smile at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    hide saku
    show rei neutral at right2, chara_enter_right
    with dissolve
    narrator "下午，湖面被风吹得亮亮的，树影落在路边，地上是一块一块晃动的光。"
    narrator "远处有人骑车，也有人慢慢散步，空气里带着一点水边特有的凉意。"
    narrator "走到湖边的时候，风吹得很舒服。"
    hide haru
    show taku excited at left2
    taku "欸，你说在这里能不能见到沙湖神大人啊？"
    rei "你来召唤一下他。"
    hina "是《沙湖神大人求包养》吗？我也玩过那个欸。"
    hide haru
    show taku excited at left2
    taku "我去，你居然也玩过，看不出来啊。"
    hide rei
    show saku neutral at right2, chara_enter_right
    saku "我也玩过，实在是太阴了，玩一半就受不了退了。"
    taku "欸诶诶，我可不允许你这么说我们沙湖神大人！"
    saku "……这玩意还有死忠粉。"
    narrator "大家就这么有一搭没一搭地聊着天，氛围意外地让人舒服。"
    narrator "Taku边走着还时不时拍照，嘴里嚷嚷着“欸回去要把这个素材加进去”。"
    narrator "突然，他又停了下来，转头看向我们。"
    taku "各位，我又有个想法了。"
    taku "我说真的，你们不觉得这里特别适合录点环境音吗。"
    hide taku
    show haru thinking at left2
    haru "环境音？"
    hide haru
    show taku excited at left2
    taku "对啊。"
    taku "风声、水声、树叶声，还有远一点的人声。"
    taku "这种东西加进去，超有氛围感啊。"
    hide rei
    hide saku
    show suzu thinking at right2, chara_enter_right
    with dissolve
    suzu "这个想法倒是不错。"
    hide suzu
    show rei smile at right2, chara_enter_right
    hide suzu
    with dissolve
    rei "难得说了句有用的。"
    taku "喂，你们对我这个创意担当真的很没有敬意啊。"
    narrator "不过吐槽归吐槽，大家还是停下来，真的让他录了一会儿。"
    narrator "风吹过湖面的时候，水声很轻。树叶沙沙地响，远处偶尔还有自行车经过的声音。"
    narrator "这种东西平时不注意，可一旦认真去听，就会觉得还挺适合放进游戏里的。"
    narrator "录了一会儿后，Taku像是又突然想到了什么。"
    taku "等等，既然都录了，那干脆连脚步声也录一下吧！"
    hina "脚步声也要吗？"
    taku "当然要啊。"
    taku "想要让别人玩的时候有身临其境的感觉，脚步声是必不可少的呀。"
    narrator "说得头头是道，我们几个都停了下来，看着他很有自信地说“你们看我的”。"
    narrator "然后，他就在石板路上走出了一串极其夸张的脚步声。"
    narrator "一步重，一步轻，中间还莫名其妙顿了一下，像什么马上要去赴一场生死约会的男主角。"
    hide rei
    show haru smile at right2
    haru "……你在干嘛？"
    taku "录脚步声啊。"
    hide haru
    show rei serious at right2, chara_enter_right
    rei "你听听这像是正常人走路的声音吗。"
    hina "太刻意了啦……！"
    narrator "我也绷不住了。"
    narrator "看着他那副一本正经搞抽象的样子，真的太好笑了。"
    taku "不是，你们懂不懂什么叫情绪？"
    hide taku
    show haru smile at left2
    haru "我们游戏里暂时还不需要这么有情绪的脚步声。"
    hide rei
    show suzu smile at right2, chara_enter_right
    hide rei
    with dissolve
    narrator "这下连Suzu都低头笑了一下。"
    narrator "最后，脚步声当然还是重录了，而且是Rei很嫌弃地亲自示范了一遍什么叫正常走路。"
    narrator "湖边的风吹过来，带着一点水汽。"
    narrator "前几天压在每个人身上的那层东西，也在一阵阵的笑声里慢慢散掉了。"
    hide taku
    hide hina
    hide saku
    hide suzu
    hide haru
    with dissolve
    scene bg shahu_park_path_day
    with Dissolve(0.8)
    show haru neutral at left1, chara_enter_left
    show suzu neutral at right1, chara_enter_right
    with dissolve
    narrator "沿湖的小路上，大家继续往前走的时候，我慢慢注意到，Suzu落在了后面一点。"
    narrator "他看着前面的湖面和树影，神情难得地有点放松。"
    haru "你怎么一个人走后面？"
    suzu "没什么。"
    suzu "可能就是想慢一点。"
    narrator "风从湖那边吹过来。"
    narrator "前面Taku还在大声嚷嚷“这个地方真的很有 gal 感”，Hina和Saku站在一棵树旁边看刚刚拍的照片，Rei一边听一边很敷衍地嗯了两声。"
    haru "你今天看起来心情挺好的。"
    suzu "……有吗？"
    narrator "我很肯定地点头。"
    haru "而且是那种，真的有在放松的感觉。"
    narrator "他没立刻说话，只是看着前面水面上晃动的光。"
    suzu "其实我挺喜欢现在这样。"
    haru "现在这样？"
    suzu "嗯。"
    suzu "大家一起出来，顺便聊项目，顺便走走。"
    suzu "不用一直盯着进度，也不用每一分钟都想着还有什么没做完。"
    suzu "反而会觉得……很轻松。"
    narrator "这句话从他嘴里说出来，还真有种很微妙的感觉。"
    narrator "毕竟前段时间，他看起来完全像是那种会把“轻松”两个字自动从生活里删掉的人。"
    haru "那不挺好嘛。"
    show suzu smile at right1
    suzu "嗯。"
    narrator "这次，他是真的很自然地笑了一下。"
    narrator "比以前那些很浅的笑意要柔和得多。"
    suzu "以前我大概不会想到，做项目的时候还能有这种时候。"
    haru "现在知道也不晚。"
    stop music fadeout 3.0
    narrator "他没再接话，只是轻轻应了一声。"
    hide haru
    hide suzu
    with dissolve
    scene bg convenience_store_night
    with Dissolve(0.8)
    show taku neutral at left2, chara_enter_left
    hide taku
    show rei neutral at left2, chara_enter_left
    show haru neutral at center, chara_enter_fade
    show hina neutral at right2, chara_enter_right
    hide hina
    show suzu neutral at right2, chara_enter_right
    with dissolve
    play music "bgm/huanghun.mp3" volume 0.3 loop fadein 1.0
    narrator "晚上，录音录到天色彻底暗下来以后，我们才慢慢往回走。"
    narrator "路边灯已经亮了，玻璃门映着暖色的光。"
    narrator "大概是吹了太久风，等真正走到便利店门口时，所有人都默契地停了下来。"
    hide suzu
    show taku neutral at right2, chara_enter_right
    taku "我饿了。"
    rei "你今天哪一秒不饿？"
    taku "你这样说就很伤人了。"
    haru "那进去买点吃的吧。"
    narrator "我们几个人一起进了便利店。"
    narrator "冰柜开开合合的声音，收银台那边“滴”地扫条码，还有货架间那种很明亮的灯光，都让人莫名觉得很安心。"
    narrator "Taku抱了一堆薯片和饭团，一副准备囤货过冬的架势。"
    narrator "Rei拿了咖啡和三明治，目标明确得不得了。"
    narrator "Hina在甜品柜前认真犹豫了半天，最后还是拿了布丁。"
    narrator "Suzu选得很简单，饭团、热饮，还有一根能量棒，看起来就很符合他的风格。"
    narrator "而Saku拿了两盒草莓牛奶。"
    hide rei
    show saku neutral at left2, chara_enter_left
    with dissolve
    haru "你喜欢这个啊？"
    saku "……还行吧。"
    narrator "她应了一声，然后停了两秒，把其中一盒递给我。"
    saku "给你一盒。"
    haru "欸？给我吗？"
    saku "刚好买一赠一。"
    saku "……你不喜欢这个吗。"
    narrator "我怔了一下，赶紧接过来。"
    haru "没有啦，我也很喜欢。"
    narrator "她没说什么，只是很轻地点了下头。"
    narrator "我们最后没急着回去，而是坐在便利店外面的长椅和台阶边，一边吃东西一边聊天。"
    narrator "那种感觉特别自然。"
    narrator "大家只是想到什么说什么。"
    narrator "说今天录音的时候谁笑得最夸张，说湖边哪块地方确实很适合放进游戏背景里，说食堂最近的菜越来越离谱。"
    narrator "也说，如果以后真的把这个游戏继续做完整，最先想让谁试玩。"
    narrator "风轻轻吹过来，带着一点夜里的凉意。"
    narrator "便利店门口偶尔有人进出，玻璃门开合之间会带出一阵冷气。"
    narrator "而我们就这样坐在那里，手里拿着吃的，慢慢地聊着天。"
    hide taku
    hide saku
    hide haru
    hide hina
    hide suzu
    with dissolve
    with None
    scene bg black
    with Dissolve(0.8)
    scene bg meeting_room_evening
    with Dissolve(1.0)
    show taku neutral at left2, chara_enter_left
    hide taku
    show suzu serious at left2, chara_enter_left
    show haru neutral at center, chara_enter_fade
    show hina serious at right2, chara_enter_right
    hide hina
    show saku neutral at right2, chara_enter_right
    with dissolve
    narrator "晚上，桌面已经乱得快没有多余位置了。"
    narrator "电脑、平板、打印稿、便利贴、咖啡、数据线，还有被来回改过很多遍的展示流程，全都堆在一起。"
    narrator "外面早就黑透了，讨论室里的灯却亮得很足，把每个人面前那一小块地方照得很清楚。"
    narrator "转眼就到了最后一天，快得有点不真实。"
    narrator "前几天还在想“还有这个没做、那个没定”，结果一眨眼，已经到了要把所有东西都收进最后版本里的时候。"
    narrator "Hina坐在桌边改文本，笔记本摊开着，旁边密密麻麻写满了修改标记。"
    narrator "Rei在电脑前调代码和打包，屏幕上的窗口一个接一个切。"
    narrator "Saku戴着耳机，平板上是最后一张CG，颜色已经铺得差不多了。"
    narrator "而Suzu和Taku坐在一起，正在讨论明天展示时到底要怎么讲。"
    hide saku
    show taku neutral at right2, chara_enter_right
    taku "这里要不要先放试玩，再讲项目思路？"
    suzu "不行。"
    taku "又不行？"
    suzu "先讲思路，老师和同学才能更快进入状态。"
    suzu "试玩放在中间，效果会更好。"
    taku "行吧，那最后结尾呢？"
    suzu "你开场，我补制作和结构部分。"
    narrator "他一边说一边在纸上改顺序。"
    suzu "最后收尾让Haru来。"
    show haru troubled at center
    haru "……我？"
    taku "组长不收尾，难道我收吗？"
    hide saku
    hide taku
    show rei neutral at right2, chara_enter_right
    with dissolve
    rei "你收尾的话，可能会把好好的展示讲成脱口秀。"
    hide suzu
    show taku annoyed at left2
    taku "你们对我的偏见真的太深了。"
    narrator "但不管怎么说，PPT和讲稿还是一点点做出来了。"
    narrator "大家都没什么空闲说笑。"
    narrator "可那种安静并不是压抑的。"
    narrator "深夜，时间已经晚到连手机上的数字都看起来有点陌生了。"
    narrator "Taku趴在桌边，嘴上还说着“我还能战”，但眼皮已经明显快撑不住了。"
    narrator "Hina轻轻揉了揉眼睛，Rei敲键盘的手也慢了一些。"
    narrator "Suzu虽然还坐得很直，但看着也有点累了。只有Saku看起来相对清醒。"
    narrator "我抬头看了一圈，决定还是先救命比较重要。"
    haru "Saku，我们俩去买咖啡吧。"
    hide rei
    show saku neutral at right2, chara_enter_right
    with dissolve
    saku "……好。"
    hide taku
    hide suzu
    hide haru
    hide hina
    hide saku
    with dissolve
    with None
    scene bg black
    with Dissolve(0.8)
    $ renpy.pause(0.5, hard=True)
    scene bg convenience_store_night
    with Dissolve(0.8)
    show haru smile at left1, chara_enter_left
    show saku neutral at right1, chara_enter_right
    with dissolve
    narrator "夜里的校园，路灯把地面照得一截亮一截暗，风比白天凉了不少。"
    narrator "周围很安静，偶尔只能听见远处一点模糊的人声。"
    narrator "我和Saku并排往便利店那边走。"
    narrator "一开始谁都没说话。"
    narrator "但这种安静并不尴尬，更像是都已经很习惯彼此在旁边了。"
    narrator "买完咖啡往回走的时候，Saku忽然开口了。"
    saku "这段时间，我还挺开心的。"
    narrator "我转头看她。"
    narrator "她低头提着袋子，声音很轻，像是在说一件不太习惯说出口的事。"
    saku "以前我从来没有这样和别人一起做过东西。"
    saku "就算是那种小组作业，也都是表面上说合作，实际上各做各的。"
    saku "我一开始也没对这个组抱有什么期待。"
    saku "但我真的没想到，我们是真的会一起讨论、一起改、一起着急，也会因为同一个东西高兴起来。"
    narrator "夜风吹过来，把她耳边的头发轻轻吹起来一点。"
    saku "我以前……也没有朋友。"
    narrator "我听着，一下子有点说不出话来。"
    saku "一开始被分到这个组的时候，我也只觉得很烦。"
    saku "我只是觉得，反正也就是把事情做完，然后结束。"
    saku "不过现在不一样了。"
    show saku smile at right1
    saku "跟你们待在一起，还挺开心的。"
    saku "而且，我也有了像你这样的朋友。"
    narrator "我的脚步一下子慢了半拍。"
    saku "……我真的很开心。"
    show haru shy at left1
    haru "……怎么突然说这种话。"
    saku "我可是很认真的。"
    haru "我知道啊。"
    show haru smile 
    narrator "我忍不住笑了一下。"
    haru "所以我才更开心呀。"
    haru "能和你成为朋友，我也特别特别高兴。"
    narrator "Saku别过脸，耳朵一点点红了。"
    narrator "……嗯，这个人果然还是很不经夸。"
    hide haru
    hide saku
    with dissolve
    scene bg teaching_building_corridor_dusk
    with Dissolve(0.8)
    show haru neutral at left1, chara_enter_left
    show saku neutral at right1, chara_enter_right
    with dissolve
    narrator "讨论室门口的走廊很安静，门缝里透出一点暖白色的灯光。"
    narrator "我刚想推门进去，Saku却忽然叫住了我。"
    saku "哦对了。"
    haru "嗯？"
    narrator "她低头从包里拿出了一个透明文件袋，动作很小心，像里面装着什么特别重要的东西。"
    narrator "然后递给我。"
    saku "这个，给你。"
    haru "什么啊？"
    narrator "我接过来，低头看了一眼。"
    narrator "下一秒，整个人都愣住了。"
    narrator "纸上是熟悉得不能再熟悉的画风。"
    narrator "右下角，还有那个我看过不知道多少遍的签名。"
    narrator "——miyako。"
    show haru surprised at left1
    haru "……等一下。"
    haru "这、这不会是……"
    saku "嗯。"
    saku "亲笔手稿。"
    saku "有签名的。"
    narrator "我脑子空白了两秒，然后差点原地叫出声。"
    show haru excited at left1
    haru "真的假的？！"
    narrator "声音没收住，我赶紧又压低一点，可整个人已经完全冷静不下来了。"
    haru "这是 miyako 老师的手稿诶？！真的？！"
    haru "我真的可以收吗？！"
    narrator "激动得太过头，我几乎是下意识抓住了她的手。"
    haru "这也太珍贵了吧！！"
    show saku shy at right1
    narrator "Saku明显被我的反应弄得有点慌。"
    saku "还、还好啦。"
    saku "也没什么……"
    haru "这怎么会没什么啊！"
    narrator "我感觉自己现在的表情一定特别夸张，可那也没办法。"
    narrator "这可是 miyako 老师，还是亲笔手稿加签名。"
    narrator "我都快感动得当场升天了。"
    haru "我会好好珍藏一辈子的。"
    show saku smile at right1
    saku "……这么夸张。"
    narrator "虽然嘴上这么说，但她还是很轻地笑了。"
    hide haru
    hide saku
    with dissolve
    with None
    scene bg black
    with Dissolve(0.8)
    centered "{color=#fff}把文件袋收好以后，我才重新去推那扇门。{/color}"
    $ renpy.pause(0.5, hard=True)
    scene bg meeting_room_evening
    with Dissolve(0.8)
    narrator "深夜，我和Saku推门进去的时候，里面安静得出奇。"
    narrator "电脑屏幕还亮着，PPT停在最后一页，代码窗口也还开着。"
    narrator "桌上散着打印稿、笔、空掉的咖啡罐，还有几张写到一半的便签。"
    narrator "而本来应该还在撑着的人——都睡着了。"
    narrator "Taku趴在桌上，脸压着自己那份讲稿，手里还抓着笔。"
    narrator "Hina枕着手臂，侧着头睡得很安静。"
    narrator "Rei靠在椅背上，眼镜都还没摘。"
    narrator "Suzu则伏在桌边，面前摊着改了一半的展示顺序。"
    narrator "那一瞬间，我和Saku都不约而同地放轻了脚步，像怕把这点安静打碎一样。"
    narrator "我把买回来的咖啡一杯杯放到桌上，动作很轻。"
    narrator "灯光落下来，把他们的侧脸照得很柔和。"
    narrator "明明桌面乱得一塌糊涂，可不知道为什么，看起来却一点都不狼狈。"
    narrator "反而让人觉得很温暖。"
    narrator "大概是因为，这种乱七八糟本身就说明了一件事。"
    narrator "他们是真的一直待到了最后一刻。"
    narrator "一直撑着、改着、做着，直到再也撑不住，才就这么趴在桌上睡着了。"
    show saku neutral at left2, chara_enter_left
    show haru troubled at right2, chara_enter_right
    saku "明明刚才还说要继续。"
    haru "结果还是全倒下了。"
    narrator "我们对视了一眼，都很轻地笑了。"
    narrator "那笑声很浅，浅得几乎要融进空调的风声里。"
    stop music fadeout 3.0
    narrator "可我站在那一刻，却忽然觉得，这可能是这段时间里，我最喜欢的一个画面。"
    with None
    scene bg black
    with Dissolve(0.8)
    centered "{color=#fff}第二天终于来了{/color}"
    play music "bgm/newpath.mp3" volume 0.5 loop fadein 1.0
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}轮到我们把这一切带上讲台了。{/color}"
    $ renpy.pause(0.8, hard=True)
    scene bg classroom_day
    with Dissolve(0.8)
    show hina troubled at left2, chara_enter_left
    hide hina
    show taku serious at left2, chara_enter_left
    show haru troubled at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    hide saku
    show suzu serious at right2, chara_enter_right
    with dissolve
    narrator "第二天下午，多媒体教室里比平时更吵一些。"
    narrator "投影亮着，前面的组正在展示。"
    narrator "后排有人低声说话，也有人翻着自己的讲稿，空气里有种很明显的“大家都在等轮到自己”的紧张感。"
    narrator "轮到我们之前，我一直觉得自己还算镇定。"
    narrator "可等真正坐在位置上，看着老师一组一组往下叫，我才发现——还是会紧张。"
    narrator "而且是那种非常真实、完全压不下去的紧张。"
    hide suzu
    show hina troubled at right2, chara_enter_right
    hina "怎么办，我好紧张……"
    taku "别慌别慌。"
    taku "我们昨天都熬成那样了，总不能今天死在最后一步吧。"
    hide hina
    show suzu serious at right2, chara_enter_right
    suzu "你说得一点安慰作用都没有。"
    taku "我这不是在稳定军心吗。"
    narrator "话是这么说，可他自己的声音其实也有点发飘。"
    narrator "Suzu低头看着打印出来的展示稿，最后又顺了一遍流程。"
    narrator "Saku坐在旁边，手指轻轻搭在平板边上，平时就不怎么显露情绪的人，这会儿看起来更安静了。"
    narrator "我深吸了一口气，又缓缓吐出来。"
    call screen timed_choice(
        "老师快点到我们组了。你要怎么调度最后这几分钟？",
        [
            ("快速统一分工并打气。", "rally"),
            ("按原计划稳步执行。", "steady"),
        ],
        timeout=6.0,
        timeout_value="timeout"
    )
    $ chapter4_choice = _return

    if chapter4_choice == "rally":
        $ team_cohesion_score += 1
        haru "最后一次确认：开场Taku，结构Suzu，收尾我。我们一起上。"
        narrator "几个人几乎同时点头，紧张感还在，但节奏立住了。"
    elif chapter4_choice == "steady":
        narrator "我没有临时改计划，只按既定流程把最后一遍顺完。"
        narrator "大家都没多说话，但动作明显更稳。"
    else:
        $ team_cohesion_score -= 1
        narrator "我迟疑了一下，大家都在等那句最终确认。"
        narrator "气氛短暂发紧，直到老师念到我们组才匆忙起身。"

    if team_cohesion_score >= 2:
        $ ending_type = "good"
    elif team_cohesion_score >= 0:
        $ ending_type = "neutral"
    else:
        $ ending_type = "bad"

    narrator "就在这时，老师念到了我们组。"
    hide hina
    hide taku
    hide haru
    hide saku
    hide suzu
    with dissolve

    if ending_type == "bad":
        jump chapter_4_presentation_bad
    elif ending_type == "neutral":
        jump chapter_4_presentation_neutral

    show teacher neutral at left2, chara_enter_left
    t "Group seven, please come to the front."
    scene bg classroom_day
    with Dissolve(0.5)
    show taku serious at left2, chara_enter_left
    show haru neutral at center, chara_enter_fade
    with dissolve
    narrator "我们几个人一起站到前面的时候，我心跳快得有点夸张。"
    narrator "教室里一下子安静了很多。"
    narrator "投影幕布亮着，标题页出现在屏幕上。"
    narrator "《Six Harmonies》。"
    narrator "下面是那句我们最开始就定下来的概念说明：六个人一起制作一款游戏的故事。"
    narrator "负责开场的是Taku。"
    narrator "他把电脑接上投影，调整好页面，然后抬头看向老师和台下的同学。"
    taku "Good afternoon. We are Group Seven."
    taku "Today, we would like to present our visual novel project, Six Harmonies."
    taku "Our story is about six students with very different personalities who are assigned to work together on a game project."
    taku "At the beginning, they do not really understand one another."
    taku "But through discussion, conflict, cooperation, and time spent together, they gradually become closer."
    narrator "他说得很顺畅，没有故作轻松，也没有乱发挥。"
    narrator "台下原本还有一点小小的杂音，这会儿也慢慢安静了下来。"
    taku "We wanted the story to feel natural."
    taku "Instead of using dramatic events, we tried to build emotional change through everyday collaboration."
    narrator "我站在旁边，忽然有点想笑。"
    narrator "因为“everyday collaboration”这种词，从他嘴里说出来居然也挺像那么回事。"
    narrator "接下来是Suzu。"
    show suzu serious at right2, chara_enter_right
    suzu "In terms of production, we tried to keep the structure clear and manageable."
    suzu "We focused on one main route, used a campus setting that we could directly reference, and controlled the scope so that the project could be completed within a limited time."
    suzu "We also discussed how to balance narrative quality and feasibility."
    suzu "Some ideas were interesting, but not all of them could be included in the final version."
    suzu "So we had to keep adjusting the content based on both creative goals and production reality."
    narrator "他的语速不快，发音也很清晰。"
    narrator "讲到制作思路、资源分配和进度控制的时候，逻辑非常稳。"
    narrator "台下有人轻轻点头，老师也一直在看我们这边，没有打断。"
    narrator "然后，终于到了试玩展示。"
    narrator "Rei把试玩版本打开的时候，我心里一下子又提了起来。"
    narrator "毕竟昨晚虽然已经做了最后调整，但那毕竟是我们这个游戏。"
    narrator "谁也不能百分之百保证，它不会在这种最关键的时候，突然给我们来一点惊喜。"
    narrator "拜托了，这次千万别再突然把立绘放到占满全屏……"
    narrator "好在，游戏运行得很顺。"
    narrator "标题画面出来了。背景切换正常，BGM正常，对话框正常，角色立绘也老老实实待在该在的位置上。"
    narrator "我心里那口气终于稍微松下去一点。"
    narrator "教室里的投影幕布上，开场画面一点点展开。"
    narrator "Hina写的那段开头，在音乐和画面配合下比平时更有氛围。"
    narrator "Saku的人设和UI颜色放在一起很统一，整体感觉很稳。"
    narrator "Rei接进去的节奏也很好，文字和切换都很顺。"
    narrator "到第一个选择点出现的时候，前排甚至有同学明显往前坐了一点。"
    narrator "有人小声说：“哇塞，这个感觉真不赖欸。”"
    narrator "也有人说：“好高的完成度。”"
    show taku neutral at left2
    taku "Here, player choice is not only interactive, but also helps express subtle emotional distance between characters."
    narrator "试玩结束以后，教室里短暂地安静了一下。"
    narrator "然后，有人开始鼓掌了。"
    narrator "不是那种很敷衍的、意思一下的掌声。"
    narrator "是真的有人看完以后，下意识鼓起了掌。"
    narrator "而且很快，其他人也跟着一起鼓了起来。"
    narrator "那一瞬间，我鼻子忽然有点酸。"
    narrator "因为直到这时，我才终于真正有了“我们真的做完了”的实感。"
    narrator "轮到我收尾的时候，我往前走了一步。"
    narrator "说不紧张是假的。"
    narrator "可当我抬头看见幕布上的标题，看见身边站着的他们，又看见台下那些正在认真看着我们的人时，心里反而慢慢稳下来了。"
    show haru serious at center
    haru "When we first got this assignment, it felt difficult."
    haru "We had limited time, different ideas, and very different personalities."
    haru "But as we worked together, we realized that making a game is not only about finishing tasks."
    haru "It's also about listening, adjusting, trusting each other, and continuing even when things get difficult."
    narrator "我的声音一开始还有点紧。"
    narrator "可说到后面，反而越来越顺了。"
    narrator "因为这些话，本来就不是硬想出来的。"
    narrator "而是这两周里，我们真的一步一步走过来的东西。"
    haru "This project was not always easy."
    haru "There were disagreements, pressure, and many things we had to revise again and again."
    haru "But because everyone contributed something important, this project was able to become real."
    haru "And for us, this is not just a class assignment."
    haru "It is something six people created together."
    haru "Thank you."
    narrator "最后一个词落下的时候，我自己都能听见心跳声。"
    narrator "可下一秒，教室里又响起了掌声。"
    narrator "这次比刚刚还要更明显一点。"
    narrator "我转头看向身边的人。"
    narrator "Taku在笑，Hina眼睛亮亮的，Rei很轻地呼了口气，Saku低着头，可嘴角明显是扬着的。"
    narrator "而Suzu站在那里，神情比平时柔和了很多。"
    narrator "那一瞬间，我忽然觉得——足够了。"
    narrator "不管最后成绩怎么样，至少这一刻，我们已经把该做到的东西，都认真地做到最后了。"
    hide taku
    hide suzu
    hide haru
    hide saku
    hide hina
    with dissolve
    scene bg teaching_building_corridor_dusk
    with Dissolve(0.8)
    narrator "从讲台前走回座位，再从教室里出来，整个过程都像还有点不真实。"
    narrator "直到站到走廊上，被外面的风一吹，我才终于慢慢有了“啊，结束了”的感觉。"
    narrator "老师后来的评价很好。"
    narrator "他说我们的主题很明确，完成度也比预想中高。"
    narrator "最重要的是，他能感觉到，这个项目不是单纯把任务拆给不同的人去做完的。"
    narrator "而是真的有“团队一起完成”的痕迹。"
    narrator "我听到这句话的时候，心里忽然轻轻动了一下。"
    narrator "因为如果是最开始的我们，大概谁也不会想到，最后会被用这种话来形容。"
    narrator "那时候的我们，甚至连坐在一张桌子边上都还带着点陌生和别扭。"
    narrator "可现在，居然真的已经走到了这里。"
    scene bg campus_path_dusk
    with Dissolve(1.0)
    show rei neutral at left2, chara_enter_left
    hide rei
    show taku smile at left2, chara_enter_left
    show hina smile at center, chara_enter_fade
    show saku smile at right2, chara_enter_right
    hide saku
    show suzu smile at right2, chara_enter_right
    with dissolve
    narrator "傍晚，太阳已经慢慢往下落了。"
    narrator "教学楼外的人来来往往，树影被拉得很长，风吹过来的时候，叶子会发出很轻的响声。"
    narrator "和最开始那天相比，校园其实没什么变化。"
    narrator "可我知道，还是不一样了。"
    narrator "这两周里，我们一起争过、笑过、卡住过，也一起熬过夜。"
    narrator "中间当然也有很难受的时候。"
    narrator "有说错话的时候，有彼此理解不了的时候，也有过一瞬间觉得“是不是要搞砸了”的时候。"
    narrator "可到最后，我们还是一起把它做完了。"
    narrator "不是因为谁一个人特别厉害，也不是因为从头到尾都很顺利。"
    narrator "而是因为每个人都在自己的位置上，认真地往前走了一点。"
    narrator "然后那些“一点”，最后就真的拼成了完整的东西。"
    narrator "我抬起头，看见他们几个人正站在前面等我。"
    narrator "Taku正在朝我挥手，表情看起来又像是准备说什么多余的话。"
    narrator "Hina抱着本子，笑着看过来。"
    narrator "Rei站在旁边，还是那副“快点，不然我先走了”的样子。"
    narrator "Saku安静地站着，发尾被风吹得轻轻晃了一下。"
    narrator "Suzu回过头，目光落在我身上。"
    narrator "我忽然觉得，Six Harmonies 这个名字，好像真的挺适合我们的。"
    narrator "六个人，六种完全不一样的声音。"
    narrator "最开始的时候，谁都不太合拍。"
    narrator "可是在不断碰撞、靠近、磨合以后，还是一点点拼成了现在这个样子。"
    narrator "也许并不完美。"
    narrator "可那的确是只有我们才能做出来的东西。"
    hide rei
    hide taku
    hide hina
    hide saku
    hide suzu
    with dissolve
    with None
    scene bg black
    with Dissolve(1.0)
    stop music fadeout 2.0
    centered "{color=#fff}而故事写到这里，也差不多该结束了。{/color}"
    play music "bgm/canopy.mp3" volume 0.25 loop fadein 1.0
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}不是因为之后什么都不会再发生。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}而是因为，有些东西走到这里，就已经足够完整了。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}比如这部被我们一起做出来的游戏。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}比如那间亮到很晚的讨论室。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}比如以后再想起这段时间时，脑子里会先浮现出来的。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}是围在一起看最初版本时忍不住笑出来的样子，是湖边吹过来的风。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}是便利店门口的夜宵，也是最后那天，趴在桌上睡着的一群人。{/color}"
    $ renpy.pause(0.8, hard=True)
    call show_chapter_end_card("第四章", "最后几天，像夏天一样慢慢过去了") from _call_show_chapter_end_card_ch4_good
    $ good_ending_card_text = replace_project_text("{size=64}{color=#FFFFFF}{b}《Six Harmonies》{/b}{/color}\n{size=34}{color=#FFFFFF}{b}好结局：和声成章{/b}{/color}{/size}")
    show text "[good_ending_card_text]" as final_end_card at truecenter
    with Dissolve(0.8)
    pause
    hide final_end_card
    with Dissolve(0.5)
    return


label chapter_4_presentation_neutral:
    show teacher neutral at left2, chara_enter_left
    t "Group seven, please come to the front."
    scene bg classroom_day
    with Dissolve(0.5)
    show taku serious at left2, chara_enter_left
    show haru neutral at center, chara_enter_fade
    with dissolve

    narrator "我们按计划完成了展示，流程基本顺下来，但每个人都明显比平时更拘谨。"
    narrator "试玩环节能跑通，不过有几处节奏和转场显得有点生硬。"
    narrator "台下的反应不算差，也不算特别热烈。"
    narrator "老师最后给了通过评价。"
    narrator "他说我们的框架完整、任务也按时交付，但团队之间的配合感还不够自然。"
    narrator "那句“你们是把项目做完了”，听上去更像一种客观陈述。"

    hide taku
    hide suzu
    hide haru
    hide saku
    hide hina
    with dissolve

    scene bg teaching_building_corridor_dusk
    with Dissolve(0.8)
    narrator "走出教室后，大家都松了口气。"
    narrator "可那种松弛更像是“终于结束了”，而不是“一起完成了什么”。"
    narrator "我们互相说了辛苦，也确认了都通过了这门课。"
    narrator "然后就各自收起资料，准备回去。"

    scene bg campus_path_dusk
    with Dissolve(1.0)
    show taku neutral at left2, chara_enter_left
    show haru neutral at center, chara_enter_fade
    show suzu neutral at right2, chara_enter_right
    with dissolve
    narrator "风还是和来时一样，校园也没什么不同。"
    narrator "六个人并肩走了一段路，却没有谁再提“下次一起”。"
    narrator "我们不是闹僵了。"
    narrator "只是停在了“合作过的同组同学”这一步。"

    hide taku
    hide haru
    hide suzu
    with dissolve

    scene bg black
    with Dissolve(1.0)
    stop music fadeout 2.0
    centered "{color=#fff}项目交上去了，分数也过线了。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}只是有些距离，并不会因为同一段经历就自动消失。{/color}"
    $ renpy.pause(0.8, hard=True)
    call show_chapter_end_card("第四章", "最后几天，像夏天一样慢慢过去了") from _call_show_chapter_end_card_ch4_neutral
    $ normal_ending_card_text = replace_project_text("{size=64}{color=#FFFFFF}{b}《Six Harmonies》{/b}{/color}\n{size=34}{color=#FFFFFF}{b}中性结局：并肩过关{/b}{/color}{/size}")
    show text "[normal_ending_card_text]" as final_end_card at truecenter
    with Dissolve(0.8)
    pause
    hide final_end_card
    with Dissolve(0.5)
    return


label chapter_4_presentation_bad:
    show teacher neutral at left2, chara_enter_left
    t "Group seven, please come to the front."
    scene bg classroom_day
    with Dissolve(0.5)
    show taku serious at left2, chara_enter_left
    hide taku
    show suzu serious at left2, chara_enter_left
    show haru troubled at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    hide saku
    show hina troubled at right2, chara_enter_right
    with dissolve

    narrator "我们站上去的时候，呼吸和节奏都没能完全对齐。"
    narrator "开场还算顺利，可试玩刚进行到中段，演示版本就出现了明显卡顿。"
    narrator "选项没有及时响应，转场也断了拍。"
    narrator "Rei紧急接管操作，Suzu也立刻补说明，但现场还是不可避免地冷了下来。"
    narrator "展示结束后，教室里先是短暂安静。"
    narrator "老师的评价很直接：项目存在关键稳定性问题，且最终呈现未达到课程要求。"
    narrator "Group Seven，本次作业判定不通过。"

    hide taku
    hide suzu
    hide haru
    hide saku
    hide hina
    with dissolve

    scene bg teaching_building_corridor_dusk
    with Dissolve(0.8)
    narrator "走廊上的风有点凉。"
    narrator "没人先开口。"
    narrator "我们都知道这句话的意思：这门课，六个人都挂了。"

    scene bg campus_path_dusk
    with Dissolve(1.0)
    narrator "后来大家只是各自收拾东西，简单说了句“回头再聊”。"
    narrator "可那天之后，我们很久都没有再坐回同一张桌子。"

    scene bg black
    with Dissolve(1.0)
    stop music fadeout 2.0
    centered "{color=#fff}有些失败，不是因为谁不够努力。{/color}"
    $ renpy.pause(0.5, hard=True)
    centered "{color=#fff}而是因为我们没能在最后关头，站成同一支队伍。{/color}"
    $ renpy.pause(0.8, hard=True)
    call show_chapter_end_card("第四章", "最后几天，像夏天一样慢慢过去了") from _call_show_chapter_end_card_ch4_bad
    $ bad_ending_card_text = replace_project_text("{size=64}{color=#FFFFFF}{b}《Six Harmonies》{/b}{/color}\n{size=34}{color=#FFFFFF}{b}坏结局：六人挂科{/b}{/color}{/size}")
    show text "[bad_ending_card_text]" as final_end_card at truecenter
    with Dissolve(0.8)
    pause
    hide final_end_card
    with Dissolve(0.5)
    return
