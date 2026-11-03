# =========================================
# chapter1.rpy
# 《Six Harmonies》第一章：风吹过白纸的时候
# =========================================
#
# 建议新增背景素材：
# 1. images/bg/campus_path_morning.png
# 2. images/bg/garden_afternoon.png
# 3. images/bg/dorm_room_day.png
# 4. images/bg/rooftop_afternoon.png
# 5. images/bg/canting.png
# 6. images/bg/garden_dusk.png
#
# 建议新增CG/演出素材（可选）：
# 1. images/cg/puff_garden_closeup.png
# 2. images/cg/empty_seat_meeting.png
# 3. images/cg/story_pitch_whiteboard.png
# 4. images/overlay/rooftop_breeze_light.png
#

label chapter_1:

    scene bg black
    with fade


    # ---------------------------------
    # 场景一：下课后的校园
    # ---------------------------------
    scene bg campus_path_morning
    with fade
    play music "bgm/happy.mp3" volume 0.15 loop fadein 1.0
    show haru neutral at center, chara_enter_fade
    with dissolve
    narrator "教学楼之间的路被太阳晒得发白，风不大，吹到人身上也没多少凉意"
    narrator "刚下课的人群从楼里陆续散出来，有人赶着去下一节课，有人低头看手机，也有人站在路边讨论作业"
    narrator "又是一个满课的早晨"
    narrator "老师在讲台上讲了什么，不能说一句都没听进去，但大概也都忘的差不多了"
    narrator "脑子里反复转的还是我们的那个项目"
    narrator "主线怎么定……分工怎么排，第二次会能不能别再像第一次一样全靠临场救火"
    narrator "还有……Saku到底在想什么"
    narrator "她昨天走出去以后，就一直没回来"

    narrator "唉，当组长真是不容易啊"

    narrator "低头看了一眼手机"
    narrator "昨天刚建好的小组群，直到现在还是零条新消息"
    narrator "明明我还专门说过，如果有想法可以随时往群里发"
    narrator "还好昨天至少把一周三次的固定开会时间定下来了"
    narrator "下一次会议是今天下午四点，现在还早"

    show haru thinking at center
    narrator "反正暂时也没别的事"
    narrator "随便走走好了"

    narrator "漫无目的地在校园里晃了一会儿，忽然想起教四后面花园里的那只三花猫"
    narrator "包里刚好还有一包猫条"

    hide haru
    with dissolve

    # ---------------------------------
    # 场景二：花园里的Saku
    # ---------------------------------
    scene bg garden_afternoon
    with fade

    narrator "教四后面的小花园"
    narrator "这里比主路安静很多"
    narrator "平时来这边的人不多"
    narrator "灌木长得有点乱"
    narrator "石板路也很窄"
    narrator "角落里有一把旧长椅，椅背上的漆已经掉了一些。"
    narrator "下午的阳光穿过树叶落了下来，光斑在树影里一点一点地晃着"
    narrator "顺着熟悉的小路走进去，看见了一个有点意外的人影"

    show saku neutral at left1, chara_enter_left
    with dissolve

    narrator "黑色外套，白色头发，蹲在花坛边上，背影冷冷的"
    narrator "是Saku"
    narrator "而那只三花猫正埋头吃着她手里的猫条，尾巴还满足地轻轻摆了摆，完全没有平时那副谨慎样"

    show haru troubled at right1, chara_enter_right
    with dissolve

    narrator "我放慢脚步走过去"
    narrator "大概是听到了声音，Saku抬头看了我一眼"
    narrator "那双眼睛还是很淡，表情也还是没什么温度"

    haru "啊……好巧啊"

    narrator "……没有比这更生硬的打招呼方式了"

    saku "……好巧"

    narrator "两个人都很努力地把气氛往更尴尬的方向推了一步"
    narrator "接下来大概有十秒钟，谁都没再说话"

    show haru neutral at right1
    haru "你经常来喂它吗？"

    saku "嗯"

    narrator "她低着头，手指轻轻顺了顺猫背上的毛，并没有抬起头来看我"

    show saku serious at left1
    saku "泡芙很胆小，只在这一块活动"
    saku "学校里认识她的人不多，也没什么人给她带吃的"

    narrator "还是第一次听她说这么多话"
    narrator "……她居然还给这只猫起了名字"

    show haru thinking at right1
    haru "泡芙？"

    show saku neutral at left1
    saku "嗯"

    haru "还挺可爱的"

    saku "……"

    show haru neutral at right1
    narrator "我也在她旁边蹲了下来，从包里掏出那包没拆开的猫条，在她面前晃了晃"

    haru "其实我也认识它"
    haru "有时候我也会给它带吃的"
    haru "不过我的记性比较差"
    haru "想起来喂它的时候，它早就已经走远了……"

    show saku neutral at left1
    saku "……这样啊"
    saku "那以后我请假不在学校的时候，也不用太担心它了"

    narrator "嗯？"
    narrator "……等等"
    narrator "这算是，她在拜托我吗？"

    show haru thinking at right1
    haru "那我这算帮上大忙了"

    narrator "故意把语气放轻松一点，顺手也拆开了猫条"
    narrator "泡芙抬头看了看我们两个，像是认真判断了一下哪边更值得信任，最后很不客气地把两边都吃了"

    narrator "我忍不住笑了一下"
    narrator "Saku也低头看着猫，脸上的表情虽然没明显变柔和，但至少不再像第一次见面时那样拒人千里"

    narrator "她其实没那么难相处……"
    narrator "就是有点像猫，得保持距离"
    narrator "等她自己确认你没威胁了，才会慢慢靠过来"

    hide haru
    hide saku
    with dissolve

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景三：睡过头与天台
    # ---------------------------------
    scene bg dorm_room_day with Dissolve(0.8)

    narrator "宿舍里"
    narrator "吃完午饭以后，我本来只是想躺一会儿，结果一闭眼，居然直接睡到了三点半"
    narrator "我猛地从床上坐起来，盯着手机上的时间看了两秒，差点怀疑自己看错了"

    narrator "完了"

    narrator "我手忙脚乱地下床，简单洗了把脸，把乱得像鸟窝一样的头发压平一点，就抓起包往会议室赶"
    narrator "结果等我赶到的时候，上一组人还没结束"
    narrator "看了眼时间，还早了几分钟"
    narrator "想了想，我干脆转身上了天台"
    stop music fadeout 1.0
    scene bg rooftop_afternoon
    with fade

    narrator "教学楼天台"
    narrator "天台的门很重，我推了半天才推开一条缝"
    narrator "风一下子迎面吹过来，带着一点高处特有的空阔感"

    show suzu serious at right1, chara_enter_right
    with dissolve

    narrator "我一抬眼，就看见了一个熟悉的背影"
    play music "bgm/cafe.mp3" volume 0.5 loop fadein 1.0
    narrator "银色的长发被风轻轻吹起来，衬衫衣角也跟着动了一下"
    narrator "Suzu一个人站在栏杆边，手里拿着手机，不知道是在看时间还是在发呆"

    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "他在我走近之前，就先回过头来了"

    suzu "你好"

    haru "……你好"

    narrator "不知道为什么，明明只是很普通的打招呼，被他说出来却总有种“这是一场正式会谈”的感觉"

    narrator "他低头看了眼表，又很自然地整理了一下衣领"

    suzu "这次会议的主题想好了吗？"

    show haru troubled at left1
    haru "嗯……等会讨论的时候再说吧"

    narrator "……压力好大"
    narrator "我甚至有种现在就该从口袋里掏出完整会议提纲的错觉"

    show suzu thinking at right1
    suzu "这次项目，比我想象中的棘手很多"

    show haru thinking at left1
    haru "你也会这么觉得啊"

    show suzu serious at right1
    suzu "当然"
    suzu "如果只是做出来，也许不算太难"
    suzu "但如果想把它做到不出错、能演示、还能让人看起来像样，就有很多地方要盯着"

    narrator "他轻轻叹了口气"

    suzu "最近还有很多别的课，还有报告，事情叠在一起，会有点难办"

    narrator "……原来你也会烦啊"
    narrator "像Suzu这种人，我还以为他的人生里只会出现“安排”和“执行”这两种状态呢"

    haru "其实，也不用给自己那么大压力吧"

    show suzu thinking at right1
    suzu "……我也经常这么提醒自己"
    suzu "不过通常没什么用"

    narrator "说完，他沉默了几秒，像是在犹豫要不要继续说下去"

    suzu "压力大的时候，我经常来这里透气"
    suzu "这里视野比较开阔，能看到整个学校"
    suzu "每次站在这儿的时候，我总会觉得，终于可以松一口气了"

    narrator "顺着他的视线看过去"
    narrator "教学楼、操场、还有穿梭在路上的人……以及稍远一点的银杏树，全都被风和阳光压成了一张很安静的风景画"

    show haru neutral at left1
    haru "这样啊"
    haru "这里确实挺适合发呆的"

    show suzu serious at right1
    suzu "我不是来发呆的"

    show haru thinking at left1
    haru "……嗯，那就是在进行高效率呼吸调整"

    pause 0.5

    show suzu smile at right1
    narrator "他说不出话来了"
    narrator "虽然只有一秒，但我很确定，他的表情空白了一下"
    narrator "然后又很轻地笑了一下"

    suzu "……差不多吧"

    narrator "这倒是今天的意外收获呢"

    show suzu serious at right1
    suzu "该下去了，要到时间了"

    haru "嗯"

    hide haru
    hide suzu
    with dissolve

    # ---------------------------------
    # 场景四：第二次会议
    # ---------------------------------
    scene bg meeting_room_day
    with fade

    narrator "教学楼一层讨论室"
    narrator "进门的时候，Taku 已经坐在那儿了，靠着椅背转笔。"
    narrator "Hina坐在另一边，笔记本已经打开，贴着颜色不同的小便签"
    narrator "Rei 还是那副样子，电脑一开，光标闪个不停。"
    narrator "Saku坐在最靠门的位置，平板放在手边，人看起来还是有点游离，但至少今天来了"

    show haru neutral at center, chara_enter_fade
    show taku excited at left2, chara_enter_left
    show hina neutral at right2, chara_enter_right
    hide taku
    show rei neutral at left2, chara_enter_left
    hide hina
    show saku neutral at right2, chara_enter_right
    with dissolve

    haru "那……开始吧"
    haru "今天主要想把主线方向再推进一点，至少确定一个能继续写下去的框架"

    hide rei
    show taku excited at left2, normal_light
    taku "那我先来！"
    narrator"taku的声音比较激动，身体微微前倾，还伸出手在空中比划"
    taku "如果只是做一个普通校园恋爱故事——当然也不是不行，但总感觉差点意思"
    taku "我们现在最大的优势，难道不是这个组合本身吗？"

    hide saku
    show hina serious at right2
    hina "组合本身？"

    taku "对啊"
    taku "会写的，会画的，会做程序的，会排期的……还有我们最强的组长"
    show haru troubled at center
    narrator "……什么叫最强的？强在哪我请问了？"

    show taku smile at left2

    taku "而且啊，我们现在这个状态本身就挺像一个故事的开头的"
    taku "一群性格完全不一样的人，被迫一起做一件事"
    taku "这不是天然的剧本吗？"

    narrator "……好想法！"
    narrator "其他人似乎也被这句话勾起了兴趣，纷纷抬起头来"

    show hina serious at right2, normal_light
    narrator "hina抬起头看了我一眼，又低下去"
    hina "我也……想过这种感觉"
    hina "一起做事的时候，关系会慢慢变化……"
    hina "就是那种比较特别的感觉吧"

    hide taku
    show rei serious at left2, normal_light
    rei "这个方向可以啊"
    rei "至少主线比单纯谈恋爱强多了"

    hide rei
    with dissolve

    show suzu serious at left2, chara_enter_left
    with dissolve
    suzu "确实啊"
    suzu "场景容易统一，资源也可以重复利用"

    narrator "太好了！大家都在积极地讨论"
    narrator "事情又有了新的进展"

    hide hina
    show saku serious at right2, normal_light

    saku "……我出去一下"

    haru "欸，等——"

    hide saku
    with dissolve

    narrator "她没等我说完，就已经推门出去了"
    narrator "讨论室里一瞬间安静下来了"
    narrator "…………"

    hide suzu
    show taku neutral at left2
    taku "……我刚刚说错什么了吗？"

    show hina troubled at right2
    hina "没有吧……"

    hide taku
    show suzu serious at left2
    suzu "先继续吧"
    stop music fadeout 2.0
    narrator "虽然会议还是继续进行"
    narrator "但总觉得，有什么地方又卡住了"
    narrator "那天的会最后还是开完了"
    narrator "我们先把“校园”“合作”“关系慢慢靠近”这些关键词记了下来，算是勉强往前走了一点"
    narrator "可直到散会，Saku也没回来"

    hide haru
    hide taku
    hide hina
    hide suzu
    with dissolve

    # ---------------------------------
    # 场景五：食堂里的Taku
    # ---------------------------------
    scene bg canting
    with fade
    play music "bgm/shitang.mp3" volume 0.15 loop fadein 1.0
    narrator "第二天中午，食堂"
    narrator "窗口前排着长队，说话声、餐盘碰撞声和广播里听不清词的流行歌混在一起，吵得很有学校食堂的风格"

    show taku smile at left1, chara_enter_left
    with dissolve

    narrator "我端着盘子，好不容易找到个空位，还没坐稳，就听见有人在后面叫我"

    taku "组长，这里！"

    narrator "…………"

    show haru neutral at right1, chara_enter_right
    with dissolve

    narrator "Taku已经坐在那边朝我挥手，旁边还放着一瓶没开封的可乐，一看就是替谁占了位置"

    haru "你怎么一个人？"

    taku "刚刚跟朋友打完招呼，他们去隔壁了"
    taku "你来的正好，我正想找人说话"

    narrator "听到这句，我心里立刻升起了不太好的预感"

    narrator "果然"
    narrator "下一秒，他就低头从包里掏出一张纸，摊在桌上"
    narrator "上面写满了密密麻麻的箭头、框和词"

    show haru troubled at right1
    haru "……这是什么"

    show taku excited at left1
    taku "我昨晚想的剧情可能性啊"
    taku "你看，如果我们的主线是几个人一起做游戏，那中间肯定得有冲突吧？"
    taku "比如意见不合、进度爆炸、有人突然消失、有人熬夜收尾，这样后面和解的时候才会更有感觉"

    narrator "他说到“有人突然消失”的时候，我莫名其妙地想到了Saku"
    narrator "为什么会想到她……"

    show haru thinking at right1
    haru "你对冲突真的很执着"

    taku "废话，没有冲突哪来的故事啊"
    taku "不过说真的，我觉得我们组还挺有戏的"
    taku "虽然每个人都怪怪的，但怪得还挺鲜明"

    haru "你这到底算夸奖还是攻击"

    show taku smile at left1
    taku "当然是夸啊"
    taku "像Rei那种，典型嘴上嫌麻烦但肯定会把东西做好的人"
    taku "Hina啊，看起来软，但执拗起来是真的谁也拦不住"
    taku "Suzu看着挺凶的吧？其实他最会照顾人了"
    taku "至于Saku……"

    taku "…………"

    taku "她是不是不太喜欢我们啊？"

    narrator "…………"
    narrator "该怎么说呢？我自己都没想明白"
    haru "……我也还在想"

    taku "不过你跟她不是说过几次话了吗？"
    taku "上次她走的时候，你看起来好像挺在意的"

    show haru serious at right1
    haru "因为她是组员啊"

    show taku neutral at left1
    taku "只是因为这个？"

    narrator "……这个人，有时候真的很会把话问到奇怪的地方"

    narrator "我低头吃了一口饭，决定不再回答"
    narrator "Taku也没再追问，只是把那张纸重新折起来，往后一靠"

    show taku smile at left1
    taku "反正啊，我还是觉得，大家再熟一点会好很多"
    taku "不然我们写“一群人慢慢理解彼此”，结果写的人之间却都不讲话，这不是很奇怪吗？"

    narrator "……说的也是"
    stop music fadeout 1.0
    hide haru
    hide taku
    with dissolve

    scene bg black with Dissolve(0.8)
    
    # ---------------------------------
    # 场景六：空出来的位置
    # ---------------------------------
    scene bg meeting_room_evening with Dissolve(0.8)
    play music "bgm/nll.mp3" loop fadein 1.0
    narrator "周五，下午四点，讨论室"
    narrator "桌上的东西比第一次开会时更多了"
    narrator "Hina带了更多便签，Rei的电脑里已经建好了几个文件夹，Suzu甚至打印了一个简易时间表，连Taku都真的带来了没有扩成十条路线的提案"
    narrator "只有一个地方是空的"
    narrator "靠门的那个位置，没有人来"

    show taku neutral at left2, chara_enter_left
    show rei serious at left1, chara_enter_left
    hide rei
    show haru neutral at center, chara_enter_fade
    show suzu serious at right2, chara_enter_right
    hide suzu
    show hina troubled at right2, chara_enter_right
    with dissolve

    narrator "四点零三分。Saku没来"
    narrator "四点零七分。Saku还是没来"
    narrator "群里也没有请假消息"

    show haru thinking at center
    narrator "我低头看了眼手机，最后还是点开聊天框，发了一句"

    haru "会议开始了，你还好吗？"

    narrator "消息发出去以后，安安静静，没有回复"

    hide hina
    show suzu serious at right2
    suzu "先开吧"

    haru "……嗯"

    narrator "我们只能先开"
    narrator "但是少了一个人，尤其是讨论视觉风格、UI设计、场景气质的时候，总觉得缺了点什么"

    show taku neutral at left2
    narrator "Taku说到一半，自己也停住了"

    taku "这个地方，本来应该问Saku的吧"

    hide suzu
    show hina serious at right2
    hina "嗯……"

    hide taku
    show rei serious at left2
    rei "先记下来，等她在的时候再确认"

    narrator "会还是继续往下推了一点"
    narrator "但是那种“大家终于开始合作了”的感觉，又被那张空椅子悄悄拉回去一些"

    narrator "散会以后，其他人陆续离开"
    narrator "我一个人多留了一会儿，把今天的记录拍照发进群里"
    narrator "还是没有回复"

    narrator "不知道为什么，我总觉得她不是单纯不想来"
    narrator "可能是某个地方出了问题？"
    narrator "如果现在不去找她，大概会一个人离我们越来越远吧"

    hide taku
    hide rei
    hide hina
    hide suzu
    hide haru
    with dissolve

    # ---------------------------------
    # 场景七：花园里的旧事
    # ---------------------------------
    scene bg garden_dusk
    with fade
    play music "bgm/machine.mp3" volume 0.5 loop fadein 1.0
    narrator "傍晚的校园，比白天安静很多"
    narrator "教学楼里的灯一间间亮起来，走廊上的脚步声变得稀疏"
    narrator "夏夜的风吹过，小路两旁的树叶沙沙作响"
    narrator "沿着花园那条小路走过去的时候，天色已经开始往橙色偏了"

    narrator "果然"

    show saku serious at left1, chara_enter_left
    with dissolve

    narrator "她在那里"
    narrator "她坐在那张旧长椅上，低着头，刚点燃一支烟"#怎么这么喜欢抽烟呢
    narrator "泡芙趴在她身后的长椅上，像是早就习惯了她的这种沉默"

    show haru neutral at right1, chara_enter_right
    with dissolve

    narrator "我放慢脚步，走到她面前"
    narrator "她听见声音，抬头和我对上了视线"
    narrator "她有点慌张地掐灭了刚点燃的烟，别过头去，没有说话"
    narrator "她的眼神比平时更迷离一点，像是整个人都陷在自己的忧郁里"

    haru "你今天没来"

    saku "嗯"

    haru "上次也是，中途就走了"

    saku "……嗯"

    narrator "她还是那副样子"
    narrator "每句话都很短，像是只愿意把门开一条缝"

    narrator "我在她旁边坐下，中间留了一点距离，没有逼得太近"
    narrator "风吹过来，把树影吹得轻轻晃了一下"

    show haru serious at right1
    haru "如果你不想说，我也不会逼你"
    haru "但你总得让我知道，问题出在哪里吧"

    narrator "这句话说完以后，她很久都没出声"
    narrator "久到我几乎以为，她会像之前那样直接起身走掉"
    narrator "可她没有"

    show saku neutral at left1
    saku "其实，我以前参加过一次差不多的项目"

    narrator "我没接话，只是安静听着"

    saku "也是分组"
    saku "几个人一起做东西"
    saku "开始的时候，大家都说得很好听，觉得一定能做完"
    saku "后来就开始不间断地争吵"

    narrator "她说得很平，平得像不是在讲自己的事"

    saku "有人觉得脚本太多，有人嫌美术太慢，有人说程序这边根本没法配合"
    saku "每次开会，都像在互相证明自己没错"
    saku "最后项目还没做完，人就先散了"

    narrator "她停了一下"
    narrator "手里的猫条包装，被她捏得发出一点很轻的响声"

    show saku serious at left1
    saku "我那时候也是画画的"
    saku "我以为只要把图画好就行"
    saku "可最后，所有人都在说问题的时候，我一句话都说不上来"

    show haru thinking at right1
    haru "……所以你觉得，是你的问题？"

    saku "不是吗？"

    narrator "她终于抬头看了我一眼"
    narrator "那双眼睛还是冷的"
    narrator "可这次冷得不一样"
    narrator "那种冷，像是把她自己也一起冻住了"

    saku "我本来也只是一个画画的"
    saku "剧情怎么写，流程怎么做，工期怎么排，那些都不是我可以决定的"
    saku "开不开会，其实也没什么区别"
    saku "我在不在，都一样"

    narrator "这句话落下来的时候，我忽然觉得有点难受"
    narrator "因为她说得太理所当然了"
    narrator "像已经把这套结论在心里重复了很多次，重复到连自己都信了"

    narrator "我想了两秒，没有立刻反驳"
    narrator "因为这种时候如果直接说“不是这样的”，多半很空"
    narrator "我低头看了一眼她脚边那只三花猫"

    show haru neutral at right1
    haru "你知道吗"
    haru "泡芙第一次见我的时候，离我至少有三米远"

    narrator "Saku愣了一下，大概没想到我会突然说这个"

    haru "我那天蹲了半天，它理都不理我"
    haru "后来还是你在，它才肯靠过来"

    narrator "她没说话"

    haru "有些东西，不是因为它不会说话，就代表它不重要"
    haru "就像你画的东西"

    narrator "我想起她平板上那几张草图，和她绘画本里那些让人难忘的画"

    haru "我们现在讨论的故事、气氛、人物关系，如果最后没有你把它们画出来，它们就只是字"
    haru "而且，不只是画出来而已"
    haru "你会在意颜色是不是太重，会在意对白框会不会压住情绪，会给一只猫起名字"
    haru "你明明比谁都知道，什么东西该怎么被看见"

    narrator "Saku的手指轻轻动了一下"
    narrator "她没有抬头，但也没有打断我"

    haru "而且，会议也不是只有决定流程的人才能参加"
    haru "或许有时候你坐在那里，一句‘这个感觉不对’，对于我们来说就已经很重要了"

    saku "……可如果最后还是会散掉呢？"

    narrator "她终于把真正卡住她的那句话说出来了"
    narrator "……她根本不相信这种团队能走到最后"

    narrator "…………"
    narrator "说实话，我也没办法拍着胸口跟她保证绝对不会"
    narrator "两周太短了，人也太不熟了，谁知道后面会不会出更多问题"
    show haru serious at right1
    haru "我不能保证我们一定不会吵架"
    haru "也不能保证中途不会出问题"

    saku "…………"

    haru "但至少现在，别一个人偷偷退出"
    haru "如果你是觉得自己无关紧要，所以不想来了……我可不答应"
    haru "你又不只是个'画画的'"
    haru "这个故事能不能成，全靠你把它画出来啊"
    haru "少了你怎么行"

    saku "…………"

    haru "而且，既然你已经在这里了"
    haru "为什么不试试看，这次会不会跟上次不一样？"

    narrator "她安静了很久"
    narrator "…………"
    narrator "她低着头，或许是天色太暗了，我看不清她的表情"
    haru "当然了，如果……"
    # narrator "眼睛被风吹得有点涩"
    # narrator "抬手去揉眼睛——"
    # narrator "等我再看过去时，她已经抬起了头"  这几句是我临时加的，但跟剧情没关系，也只能去掉，只是想起来一些事情，所以写下这几句话
    # narrator "脸上是我熟悉的那种平静"
    # narrator "但总觉得……好像错过了什么"
    show saku neutral at left1
    saku "……你说话还挺会挑重点的"
    "她打断了我的话"
    show haru thinking at right1
    haru "你是在夸我吗？"

    show saku neutral at left1
    saku "没有"

    narrator "可她说这句的时候，嘴角很轻地动了一下"
    narrator "非常轻，轻到几乎看不出来"
    narrator "但我看见了"

    saku "下次会议，我会去的"

    show haru neutral at right1
    haru "真的？"

    saku "嗯"
    saku "但如果他们又开始乱七八糟地吵，我还是有可能走掉"

    haru "……好的"

    narrator "不知道为什么，我忽然松了口气"
    narrator "那种一直吊着的感觉，总算稍微落下来一点"
    narrator "至少她没有把门彻底关上"
    stop music fadeout 1.0
    hide haru
    hide saku
    with dissolve

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景八：下一次会议
    # ---------------------------------
    scene bg meeting_room_day with Dissolve(0.8)
    play music "bgm/cafe.mp3" volume 0.5 loop fadein 1.0
    narrator "周一，下午四点，讨论室"
    narrator "门被推开的时候，里面已经坐了几个人"
    narrator "Taku在转笔，Hina在翻本子，Rei盯着电脑，Suzu在看时间表"

    show taku neutral at left2, chara_enter_left
    show hina neutral at left1, chara_enter_left
    hide hina
    show rei serious at center, chara_enter_fade
    show suzu serious at right2, chara_enter_right
    with dissolve

    narrator "我和Saku几乎是一前一后走进去"

    hide rei
    with dissolve

    show haru neutral at center, chara_enter_fade
    hide suzu
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "到门口的那一瞬间，Taku明显愣了一下"

    show taku smile at left2
    taku "哦，你来了啊"

    saku "嗯"

    narrator "我坐下以后，故意没多说什么，只是像平常一样开口"

    haru "那今天继续吧"
    haru "上次说到，故事方向可能跟‘合作做游戏’有关"
    haru "我觉得可以正式往这个方向试试看"

    narrator "这一次，Saku没有中途起身"
    narrator "虽然还是不太主动说话，但当我们讨论到画面气质、角色第一印象和对话框样式时，她还是会接几句"
    narrator "而且每一句都很有用"

    show saku serious at right2
    saku "如果要做游戏项目，UI配色得统一"
    saku "背景太花会抢主界面的焦点"

    show hina serious at left2
    hina "那用偏冷色调怎么样？"
    hina "比如深蓝或者灰紫，不会太抢眼"

    show saku neutral at right2
    saku "嗯...深蓝可以"
    saku "但饱和度别太高，不然看久了累"
    hide hina
    show rei neutral at left2
    rei "那我试试低饱和的蓝灰色"
    rei "顺便把按钮也改成同一色系"

    narrator "大家围着桌子讨论的还挺热情的"
    narrator "感觉今天挺顺啊……"
    narrator "总算有点团队的意思了"

    # ---------------------------------
    # 场景九：把我们的故事写进去
    # ---------------------------------
    narrator "讨论进行到一半的时候，白板上已经写了不少字"
    narrator "校园"
    narrator "放学后"
    narrator "合作"
    narrator "游戏制作"
    narrator "慢慢靠近"
    narrator "冲突"
    narrator "六个人"

    narrator "这些词单独看都很普通"
    narrator "可放到一起，不知道为什么，就已经有一点故事的样子了"

    hide hina
    show taku neutral at left2
    taku "所以现在的问题就是，到底写什么故事"

    hide taku
    with dissolve

    show rei thinking at left2, chara_enter_left
    with dissolve

    rei "方向其实已经差不多了"
    rei "现在还差一个足够具体的核心"

    hide rei
    show hina serious at left2
    hina "嗯"
    hina "要能把这些东西串起来"

    narrator "六个人……"
    narrator "油性笔的墨迹渗进白板表面，边缘略微晕开，有点刺眼的反光"
    narrator "我看着那三个字，看得有点出神"
    narrator "所有碎片都对上了！"

    show haru serious at center
    haru "我们就写这个吧"
    haru "把我们的故事写进去"
    haru "六个原本不熟的人，因为同一个项目被分到一组，必须一起做出一款游戏"

    narrator "房间里安静了一下"

    hide rei
    with dissolve

    hide hina
    show taku excited at left2, chara_enter_left
    with dissolve

    taku "……喔，感觉不赖诶"

    haru "一开始大家都只在意自己那部分"
    haru "有人想做得有趣，有人只想它先跑起来，有人在意情绪，有人在意画面，有人在意时间"
    haru "然后在不断合作、争执、磨合的过程中，慢慢开始理解彼此"

    hide taku
    show hina serious at left2
    hina "这样的话，角色之间的关系为什么会变近，也会显得很自然"

    haru "对啊"
    haru "因为一起做一件事，本来就会看见很多平时看不见的部分"

    narrator "Hina低头看着笔记本，嘴角不自觉地上扬了"

    show hina shy at left2
    hina "这个方向很好"
    hina "我好喜欢"
    hina "很多我原本想写的那些细碎时刻，都可以放进去了"

    hide hina
    show taku smile at left2
    taku "而且代入感很强啊"
    taku "玩家本来就在玩一款galgame，故事里的人也在做一款galgame"
    taku "这个设定可真有意思"

    hide taku
    with dissolve

    show rei serious at left2
    rei "结构好做"
    rei "主线清楚就行，分支放关系上，别整太复杂"
    hide rei
    with dissolve
    show suzu serious at left2
    with dissolve
    suzu "排期能救"
    suzu "场景集中，逻辑也收着"
    show saku serious at right2
    saku "画面的话……不会太乱"
    narrator "刚说完这话，大家都看向Saku"
    narrator "她平时不怎么表态"
    narrator "今天这一出，确实让大家震惊到了"
    show saku annoyed at right2
    saku "……看什么看" 
    hide suzu
    with dissolve
    show taku smile at left2
    taku "没事啊，挺好"
    saku "……你很烦你知道吗"
    narrator "Saku虽然嘴上这么说，但也没真走"
    narrator "而且听着也不像真生气"

    show haru neutral at center
    haru "那就这么定了？"
    haru "我们的故事，就写六个人合作完成一款游戏"

    narrator "这次，没有谁立刻提出反对"

    taku "OK"
    hide saku
    show hina serious at right2
    hina "我也赞成"
    hide taku
    show rei serious at left2
    rei "可以"
    hide hina
    show suzu serious at right2
    suzu "没问题"

    hide suzu
    show saku neutral at right2
    saku "嗯"

    narrator "……不知道是不是错觉"
    narrator "在这一瞬间我忽然觉得，这个原本只是被老师硬塞到我们面前的项目，好像终于开始长出一点属于我们自己的样子了"

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景十：散会以后
    # ---------------------------------
    scene bg meeting_room_evening with Dissolve(0.8)

    narrator "天色已经有点沉下来了"
    narrator "讨论室的灯比窗外亮得多，把白板上的字照得很清楚"
    narrator "桌上的水杯、纸和便签散得到处都是，像刚刚经历了一场不算混乱、但确实很投入的讨论"

    narrator "大家开始收东西"
    narrator "Taku还在念叨这个设定后面肯定还能长出很多有意思的桥段"
    narrator "Hina一边听一边把笔记本合上"
    narrator "Rei已经在电脑里新建好了主线文件夹"
    narrator "Suzu则低头重排时间表，嘴里还在算测试时间要提前几天留"
    narrator "Saku把平板收进包里的动作很轻"

    show haru neutral at left1, chara_enter_left
    show saku neutral at right1, chara_enter_right
    with dissolve

    narrator "我看了她一眼"
    narrator "她也刚好抬头，看见我以后，停了一下"

    saku "……今天，感觉还行"

    show haru thinking at left1
    haru "只是还行吗？"

    show saku neutral at right1
    saku "……已经算很高评价了"

    narrator "我差点笑出声"
    narrator "嗯，行吧，这确实很像她会给出的最高级别赞赏"

    hide haru
    hide saku
    with dissolve

    show taku excited at left2, chara_enter_left
    show suzu serious at left1, chara_enter_left
    hide suzu
    show hina shy at center, chara_enter_fade
    show rei neutral at right2, chara_enter_right
    hide rei
    show saku neutral at right2, chara_enter_right
    with dissolve

    taku "走不走，去校餐厅吃点夜宵，我脑子都快转空了"

    hide saku
    show suzu serious at right2
    suzu "你不是刚说灵感爆炸吗"

    taku "灵感爆炸和肚子饿又不冲突"

    hina "我……我可以一起去吗"

    hide taku
    show rei serious at left2
    rei "随便"

    narrator "几个人说着说着，居然真的就这么往外走了"
    narrator "我落在最后，顺手把白板擦了一半，又停下来，看了眼还没擦掉的那行字"
    narrator "{b}六个人合作完成一款游戏的故事{/b}"
    narrator "很普通的一句话"
    narrator "放在这里让人莫名有点想笑"
    narrator "也许是因为它听起来像是在写剧本"
    narrator "又像是在说现在的我们"

    hide taku
    hide suzu
    hide hina
    hide rei
    hide saku
    with dissolve

    narrator "我关掉讨论室的灯，跟上前面的几个人"
    narrator "走廊里，Taku的声音还是最大，Suzu时不时回一句，Hina在旁边轻轻笑"
    narrator "Rei虽然没说太多话，但也确实没有离开"
    narrator "而Saku走在最边上，表情还是淡淡的"
    narrator "不过这一次，她没有掉队"

    call show_chapter_end_card("第一章", "风吹过白纸的时候") from _call_show_chapter_end_card_ch1

    return
