# =========================================
# chapter3.rpy
# 《Six Harmonies》第三章：风平浪静之后
# =========================================
#
label chapter_3:

    scene bg black
    with fade
    play music "bgm/cafe.mp3" volume 0.5 fadein 1.0


    # ---------------------------------
    # 场景一：突击检查
    # ---------------------------------
    scene bg classroom_day
    with fade

    show teacher neutral at left2, chara_enter_left
    with dissolve

    narrator "上课铃刚响过没多久，教室里还有一点没完全收拢的杂音。投影仪亮着，窗外的阳光被窗框切成一格一格的，落在靠窗那排课桌上。"
    narrator "老师翻着手里的名单，语气和平时一样平静。"

    t '"Before class starts, I want to do a quick progress check on several groups."'

    narrator "……"
    narrator "我握着笔的手顿了一下。"
    narrator "前几天Suzu就说过，老师大概会中途抽查。只是我没想到，会来得这么突然。"

    t '"Group seven."'
    t '"Come and give me a brief update."'

    show taku neutral at right1, chara_enter_right
    with dissolve

    narrator "我心里一紧，刚想站起来，旁边的Taku已经先一步把椅子往后一推。"
    taku "交给我吧。"
    narrator "我甚至还没来得及拦，他已经拿着电脑走到前面去了。"
    narrator "……这家伙，真的一点都不会紧张吗。"

    hide taku
    with dissolve

    show taku neutral at center, chara_enter_fade
    with dissolve

    narrator "投影切到我们的项目页面。虽然现在还只是初步版本，UI 和脚本也都还在调整中，但最基本的结构已经能跑了。"
    narrator "角色设定图、部分背景参考、主线概念，还有 Hina 整理出来的剧情开头，都被做进了展示里。"

    taku '"Our project is a campus-themed visual novel."'
    taku '"It\'s about six people with very different personalities working together to create a game."'
    taku '"And through that collaboration, they gradually begin to understand each other."'

    narrator "……还挺像样。"
    narrator "他平时看着总像会在正经场合突然胡来，可真的站到前面以后，反而讲得很顺。"
    narrator "他把项目的核心主题、角色氛围、资源规划，还有目前已经完成的部分都讲了一遍。"
    narrator "连“让玩家代入一群人一起制作 galgame”这层设计趣味，他都说得很清楚。"

    t '"The concept is interesting."'
    t '"The structure is also clear."'

    narrator "我心里刚松了一口气。"

    t '"But your progress is slower than it should be."'

    narrator "……"
    narrator "Taku 脸上的笑僵了一下。"
    play music "bgm/nll.mp3" fadeout 1.0 fadein 1.0

    t '"You have a good direction."'
    t '"But direction alone is not enough."'
    t '"You are already behind schedule in terms of implementation."'
    t '"If this pace continues, you may not be able to finish a stable demo in time."'

    narrator '"behind schedule" 像一根针，轻轻扎进了本来还算松软的空气里。'

    t '"Be careful."'
    t '"Interesting ideas are valuable only when they can be delivered."'

    hide teacher
    hide taku
    with dissolve

    narrator "我们回到座位以后，已经开始上课了。"
    narrator "可我根本听不进去前面在讲什么。"
    narrator "{b}你们的进度，比该有的更慢。{/b}"

    scene bg black with Dissolve(1.0)

    # ---------------------------------
    # 场景二：被敲响的紧迫感
    # ---------------------------------
    scene bg teaching_building_corridor_day with Dissolve(0.8)

    show taku neutral at left1, chara_enter_left
    hide taku
    show haru neutral at center, chara_enter_fade
    show suzu serious at right2, chara_enter_right
    with dissolve

    narrator "下课后，人流断断续续往外走，楼道里满是鞋底摩擦地面的声音。我们几个人站在走廊边，一时间谁都没先说话。"

    show taku neutral at left2, chara_enter_left
    taku "呃……老师要求还真严格啊。"
    hide taku
    show rei neutral at left2, chara_enter_left
    rei "他也没说错。"
    narrator "……好直接。"
    narrator "Taku 的嘴角抽了抽。"

    hide rei
    show hina serious at left2, chara_enter_left
    hina "其实……我也有一点这种感觉。最近虽然一直都在推进，可真正“完成了”的东西，好像没有想象中那么多。"
    hide hina
    show saku neutral at left2, chara_enter_left
    saku "确实，立绘还没有精修。CG 也还差几张。"

    show suzu thinking at right2
    suzu "不止是这些。脚本、演出、资源整合、测试，这些东西每一项都还做得不够。"

    haru "那……晚上还是照常开会吧。先重新理一下现在的进度。"

    show suzu serious at right2
    suzu "不只是理一下。"
    suzu "我们必须要抓紧了。"

    hide taku
    hide haru
    hide suzu
    with dissolve

    scene bg black with Dissolve(1.0)

    # ---------------------------------
    # 场景三：明显失去松弛感的会议
    # ---------------------------------
    scene bg meeting_room_evening with Dissolve(1.0)

    show taku neutral at left1, chara_enter_left
    hide taku
    show haru neutral at center, chara_enter_fade
    show suzu serious at right2, chara_enter_right
    with dissolve

    narrator "白炽灯照下来，桌面亮得发白。外面已经黑了，玻璃门上映出室内模糊的倒影。桌上的纸和电脑比平时更乱一点，像每个人都带着点匆忙赶过来，连整理都顾不上。"
    narrator "这次的空气和前几次很不一样。老师那句“进度慢了”，还挂在每个人头顶，谁也没法当没听见。"

    suzu "我先说。"
    suzu "从今天开始，我们不能再像之前那样了。"
    suzu "每次开会都很松，聊着聊着就散出去，试读、闲聊、顺着感觉改东西，这些本身不是错。"
    suzu "但如果进度已经开始落后，还继续维持这种节奏，我们后面只会更危险。"

    narrator "整个房间都安静了下来。Hina 低头按住了笔记本边角，Rei 盯着屏幕，Saku 靠在椅子里，手指轻轻搭在平板边缘。"

    suzu "接下来每次会议都要明确目标。谁今天交什么，明天推进到哪一步，哪些内容必须砍，哪些内容不能再拖，都得说清楚。"

    show taku serious at left2
    taku "……也不用这么紧张吧。"
    taku "当然要认真做，但也没必要一下子变成高压工地现场。大家全都绷得太紧，反而更做不出好东西。"

    show suzu serious at right2
    suzu "所以呢？"

    taku "所以还是得留一点松弛感啊。我们这项目本来就不是流水线作业，一直这么压，写出来的东西也会越来越僵吧？"
    suzu "松弛感是建立在能交得出来的前提上。"
    taku "可你这样会让所有人都喘不过气吧？"

    narrator "桌上的气氛又开始卡住了。"
    hide suzu
    show hina serious at right2, chara_enter_right
    hina "那个……要不我们先把今晚该处理的部分定下来？"
    hide taku
    show rei neutral at left2, chara_enter_left
    rei "对，先干活。"

    haru "嗯，先别纠结抽象的问题了。今天先看脚本和立绘的衔接，还有演示段落里哪些地方要优先完成。"

    narrator "会议还是继续了下去，可那种轻松的感觉全然消失了。"
    narrator "连 Taku 后面说话都收敛了不少，不像平时那样想到什么就往外倒。Suzu 更是从头到尾绷得笔直。"
    narrator "那天的会开到很晚。问题是有推进，可没人觉得轻松。"
    narrator "散会的时候，大家收东西的动作都比平时快，像是谁都没有力气再站在门口多聊两句。"

    hide taku
    hide haru
    hide suzu
    with dissolve

    # ---------------------------------
    # 场景四：第二天，一起赶工
    # ---------------------------------
    scene bg meeting_room_day with Dissolve(0.8)

    show taku neutral at left2, chara_enter_left
    show hina serious at left1, chara_enter_left
    hide hina
    show haru neutral at center, chara_enter_fade
    show suzu serious at right2, chara_enter_right
    with dissolve

    narrator "第二天下午，讨论室里比平时还满。电脑、平板、打印稿、参考图、咖啡、便利贴，还有 Suzu 重新排过的时间表，把桌面几乎全占满了。"
    narrator "大家都来得很早。连 Taku 都没像平时那样踩点进门，而是提前十几分钟坐在那儿，手边还摊着自己整理过的分镜和剧情笔记。"

    haru "那今天就按昨天定的来。Hina 和 Taku 过一遍主线中段，确认对话和节奏；Rei 看脚本接入；Saku 那边继续细化立绘和 CG；Suzu 负责整体进度和内容删改。"
    suzu "开始吧。"

    narrator "一开始其实还挺顺利的。讨论有在推进，Hina 修改台词的时候，Taku 会补一些更有画面感的小细节；Rei 也会偶尔抬头，说某段对话切入选项的位置最好再明确一点。"

    # ---------------------------------
    # 场景五：争执升级
    # ---------------------------------
    show taku serious at left2
    taku "等等，我觉得这里还是能再加一个选项。"

    show suzu serious at right2
    suzu "加什么？"

    taku "主角和其中一个人单独留在教室那段，如果这里给玩家一个回应选项，后面关系变化会更自然一点。"
    taku "甚至可以顺手带出一个小分支，不用很长，但会让人物更立体。"

    narrator "我看到 Hina 的表情先是“好像有点道理”，然后又慢慢变成了“但是……”。"

    suzu "不行。"
    narrator "我没想到 Suzu 会拒绝得这么直接。"

    call screen timed_choice(
        "火药味开始上来。你要怎么做？",
        [
            ("立刻打断，让两个人先停一下。", "interrupt_now"),
            ("先听完，再尝试总结。", "observe_first"),
        ],
        timeout=6.0,
        timeout_value="timeout"
    )
    $ chapter3_choice = _return

    if chapter3_choice == "interrupt_now":
        $ team_cohesion_score += 1
        haru "先等一下，别急着顶回去。"
        narrator "两个人都停了半拍，语气稍微压下来了一点。"
    elif chapter3_choice == "observe_first":
        narrator "我先没插话，想把两边的点都听完整。"
        narrator "空气还是绷着，但至少没有立刻失控。"
    else:
        $ team_cohesion_score -= 1
        narrator "我没能第一时间开口，沉默把火气又往上推了一截。"
        narrator "等我反应过来时，两边已经顶到了最硬的语气。"

    taku "为什么？"
    suzu "因为这个地方现在的作用已经足够清楚了。"
    suzu "再加选项，后面的对话、变量、演出都要跟着改。你说是小分支，但工作量不会只小到你说的程度。"

    taku "可这样会更有意思啊。"
    suzu "我们现在最关键的是跟上进度。"
    taku "你又来了。"
    taku "我发现你现在真的是，什么东西第一反应都是砍掉。Suzu，你到底是想做作品，还是想做最安全的交差模板？"
    suzu "我得保证它能完成。"

    show taku annoyed at left2
    taku "可你这样什么都不敢加，最后做出来的东西会多无聊你知道吗？"
    suzu "无聊总比做不完强。"
    taku "那你干脆把我之前提的那条支线也一起删了算了。"

    narrator "Suzu 看着他，语气冷得没有起伏。"
    suzu "我本来就打算这么说。"
    suzu "你之前加的那条支线，除了让角色多说几句情绪化的对白，没有起到任何关键推进的作用。"
    suzu "它会拖慢节奏，也会增加接入和测试负担。没有什么价值。"

    narrator "桌边一下就安静了。大概连 Taku 自己也没想到，Suzu 会说得这么直接。"

    taku "“没有什么价值”？"
    taku "你说得倒轻松啊。你是不是觉得，除了排期表上的东西，别的全都可以随便划掉？"
    suzu "如果那部分确实会影响整体完成度，就应该划掉。"
    taku "卧槽，你这个人真的……"
    taku "你是不是根本就不懂创作？"

    narrator "……糟了。"
    narrator "我下意识想开口拦，可还没等我说话，Taku 已经把后面几句都砸了出来。"

    taku "还是说，你只是喜欢把大家都管得像给你打工一样？"
    taku "反正只要最后看起来够整齐、够完美，你就满意了吧？"
    taku "你根本没考虑到我们的感受，你整天除了压力人还会干什么！"

    narrator "那一瞬间，整个讨论室静得可怕。"
    narrator "我心头一紧，看向了 Suzu。"
    narrator "他没立刻反驳，甚至连表情都没怎么变。只是那种本来就很平静的神色，在那一秒彻底冷了下去。"

    show suzu thinking at right2
    suzu "……这样吗。"

    narrator "他低下头，把桌上的文件合起来，站起身。"
    haru "Suzu，等一下。"
    suzu "那你们继续吧。"
    narrator "他的声音还是平静的。平静得让人难受。"
    narrator "说完，他就转身出了门。门被关上的声音并不大，可整个房间都像是被压住了一样。"
    narrator "没人说话，连 Taku 自己都像一下子僵住了。"
    narrator "那天的工作，最后还是这么不了了之了。桌上的纸还摊着，电脑还亮着，没改完的对白和没决定好的结构，也都还停在原来的位置上。"

    hide taku
    hide hina
    hide haru
    hide suzu
    with dissolve

    scene bg black with Dissolve(1.0)

    # ---------------------------------
    # 场景六：沉默与短信
    # ---------------------------------
    narrator "第二天，上午。"
    play music "bgm/clouds.mp3" fadeout 1.0 fadein 1.0
    narrator "手机屏幕亮了又暗，群聊安静得像被冻结了一样。"
    narrator "从昨晚到现在，没有一个人讲话。没有人发“昨天先冷静一下”，也没有人发“今天还开会吗”。"
    narrator '我给 Suzu 发了消息："你还好吗？"'
    narrator "没有回。"
    narrator '过了一个小时，我又发："今天下午还来吗？"'
    narrator "还是没有回音。"
    narrator "一整个上午，我都坐立难安。只是反反复复地打开手机，又失落地按灭。"
    narrator "上午最后一节课结束后，我抱着书走出教室，脑子里还是昨晚的场景。"
    narrator "想了两秒，我转身朝食堂后面那条路走。"
    narrator "我得先找 Taku 谈谈。"

    scene bg garden_afternoon with Dissolve(0.8)

    # ---------------------------------
    # 场景七：先去找 Taku
    # ---------------------------------
    show taku serious at left1, chara_enter_left
    show haru neutral at right1, chara_enter_right
    with dissolve

    narrator "树荫把地面切成一片片晃动的光，风不大，空气却有点闷。Taku 坐在长椅一头，手里拿着一罐可乐，却半天都没打开。"
    narrator "他看见我过来，表情难得有点不自然。"

    taku "……你是来骂我的吧。"
    haru "本来有点想。"
    haru "但比起骂你，我更想知道你现在怎么想。"

    narrator "Taku 低头盯着手里的易拉罐，沉默了很久。平时那种一张嘴就停不下来的样子，好像全都不见了。"

    taku "我昨天说得太重了。"
    taku "我当时就是一下子上头了。听到他说那条支线没什么价值的时候，我真的有点火。"
    taku "可后来回去想想……他其实也没说错。"
    taku "我最近确实塞了太多想法进去。总觉得这个也想留，那个也舍不得删，好像少一点就会变得没意思。"
    taku "可我们本来就没时间。"
    taku "而且 Suzu 为了这个项目做了多少，我也不是看不见。排期、整理、补资料、盯细节……他基本把所有容易被忽略的烂摊子都先接过去了。"
    taku "……但我居然还说那种话。"

    haru "那你打算怎么办？"
    taku "道歉。"
    taku "我必须去道歉。"

    narrator "他低头拿出手机，手指停在屏幕上好一会儿，像是在想怎么把那些平时说得很顺的话，真正变成一句认真又不轻浮的道歉。"
    narrator "最后，他还是发了出去。"
    narrator "我没去看他到底写了什么，只看着他按下发送键以后，整个人往后一靠，长长呼了口气。"

    hide taku
    hide haru
    with dissolve

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景八：缺席的人
    # ---------------------------------
    scene bg meeting_room_day with Dissolve(0.8)

    show rei neutral at left2, chara_enter_left
    show hina troubled at left1, chara_enter_left
    hide hina
    show haru neutral at center, chara_enter_fade
    show taku serious at right2, chara_enter_right
    hide taku
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "下午，讨论室。大家都到了，只有 Suzu 没来。"
    narrator "四点整。没有人进门。四点零五，还是没有。群里也没有消息。"
    narrator "桌上还放着他昨天打印出来的时间表，纸边折着一个很小的角，像主人只是暂时离开，下一秒还会坐回来。"

    hide suzu
    hide saku
    show hina troubled at right2, chara_enter_right
    hina "……他还是没回吗？"
    haru "没有。"
    rei "电话呢？"
    haru "打过了，没接。"

    narrator "房间里的空气一下子沉了。Taku 低着头，手指一直摩挲着手机边缘，脸色比谁都难看。"

    haru "先开吧。总不能一直等。"

    narrator "于是会还是开了。可真的开始以后，我们才发现，没有 Suzu 在，很多东西立刻变得不一样了。"
    narrator "讨论到一半，没人能第一时间判断这个改动会不会拖工期；提到后续整合的时候，也没人能立刻把各部分的优先顺序压出来。"
    narrator "以前总觉得 Suzu 太有压迫感，像空气里那根一直绷着的线。可当那根线真的不在了，整个小组反而一下子散了。"
    narrator "大家这才更明显地意识到，很多原本能顺利往前推的东西，背后一直都有他撑着。"

    hide rei
    hide hina
    hide saku
    show taku neutral at right2, chara_enter_right
    taku "……我太过分了。"

    hide rei
    hide hina
    hide haru
    hide taku
    hide saku
    with dissolve

    # ---------------------------------
    # 场景九：去找他吧
    # ---------------------------------
    scene bg campus_path_dusk with Dissolve(0.8)

    show taku serious at left2, chara_enter_left
    show hina serious at left1, chara_enter_left
    hide hina
    show haru neutral at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "傍晚，食堂外。天色一点点暗下来，路灯开始亮了，风里带着一点晚饭时间特有的烟火气。"
    narrator "我们几个人站在门口，谁手里的筷子都没怎么动。"

    hide saku
    hide haru
    show hina serious at center, chara_enter_fade
    show saku neutral at right2, chara_enter_right
    hina "这样下去不行啊。"
    saku "先把人找到吧。"
    taku "我去找。"
    haru "不能只有你一个人去。"
    haru "我们一起去找 Suzu。"

    narrator "于是晚饭后，我们分开在校园里找他。"
    narrator "教室、图书馆、自习区、实验楼、操场边、宿舍楼下，能想到的地方都找了一遍。可哪儿都没有。"
    narrator "天色逐渐暗下来，我站在教学楼前，忽然想起第一次在天台见到他的时候。"
    narrator "……天台。"

    hide taku
    hide hina
    hide haru
    hide saku
    with dissolve

    scene bg black with Dissolve(1.0)

    # ---------------------------------
    # 场景十：天台上的 Suzu
    # ---------------------------------
    scene bg rooftop_dusk with Dissolve(1.0)

    show haru neutral at left1, chara_enter_left
    show suzu thinking at right1, chara_enter_right
    with dissolve

    narrator "夜风迎面扑过来，带着高处特有的凉意。栏杆边那个熟悉的背影就在那儿，衬衫被风吹得轻轻贴在身上，比平时看起来更单薄一点。"

    haru "……原来你在这。"
    suzu "……抱歉。"
    haru "你今天失联了一整天。"
    suzu "我知道。"
    haru "手机呢？"
    suzu "……今天一天都没看。"

    narrator "我走到他旁边，没有站得太近，只是和他一起看向楼下安静下来的校园。"
    narrator "风很大，把额前的头发都吹乱了。"

    haru "大家都在找你。"

    suzu "我今天……有点崩溃。"
    narrator "这句话从他嘴里说出来，轻得几乎要被风吹散。可越轻，越让人胸口发紧。"

    haru "是因为昨天的事吗？"
    suzu "……不只是吧。"
    suzu "我一直都知道，我有问题。"
    suzu "我太在意结果了。只要事情做得不够好、不够完整，我就会觉得前面的努力都失去了意义。"
    suzu "所以我会不自觉地盯进度、盯细节、盯所有可能出错的地方。"
    suzu "我总觉得，只要我先把一切压住，就能避免最坏的情况。"
    suzu "可最后，我反而总是在给别人压力。以前也是。"
    suzu "做项目、做活动、做任何合作的事，只要我开始控制不住地追求“必须完美”，周围的人就会越来越累。"
    suzu "我说自己是为了减少麻烦，为了不给别人增加工作量……可那样做，只会让所有人都更难受。"
    suzu "之前就是因为这样，我伤害过很多人。"
    suzu "有人说和我合作像被审判，有人说我根本不在乎别人的感受。"
    suzu "反正最后，大家都走了。"
    suzu "也许我本来就不适合这种小组项目，我本来也不适合和别人走近。"
    suzu "其实我一直都没什么朋友，不过这也正常吧。"

    narrator "这句说得太平静了。平静得像他已经这么告诉自己很久很久，久到连难过都被磨钝了。"

    haru "可你做那些事，不是为了伤害别人。"
    suzu "可是结果没有差别。到最后我还是伤害了别人。"
    haru "当然有差别。"
    haru "Suzu，你确实会因为太想把事情做好，而给周围的人压力。你也确实很容易把自己逼得太紧。"
    haru "可这不等于你是故意去伤害谁。"
    narrator "他没说话。我知道他不是会因为几句安慰就立刻好起来的人。"

    narrator "突然，天台的门被猛地推开了。"

    hide haru
    hide suzu
    show taku serious at center, chara_enter_fade
    with dissolve

    taku "靠……果然在这里。"
    narrator "他扶着门框，明显是一路跑上来的，连头发都被风和汗弄乱了。"
    narrator "平时总是话很多的人，这会儿却罕见地卡了两秒。"

    taku "昨天那句话……对不起。"
    narrator "他的语气认真得几乎有点不像平时的他。"
    taku "我说得太过了。而且我知道，那不是真的。"
    taku "你不是想控制谁，也不是想显得自己有多厉害。"
    taku "我知道的，你只是……太认真了，认真过头了。"
    taku "我昨天回去以后一直在想。"
    taku "这个项目到现在，谁做了多少、谁在顶着进度、谁总是在大家聊得最开心的时候跳出来说“先等等”，其实我全都知道。"
    taku "我只是那时候上头了，觉得自己的东西被否掉很不爽，就把最伤人的话直接丢给你了。"
    taku "这事是我错了。"
    taku "而且说实话，我那些想法本来就太多了。有些我舍不得删，不代表它们真的必须留下。"
    taku "我知道你卡我，不是因为你讨厌有趣的东西。"
    taku "是因为你真的在想，什么东西能让我们的项目顺利走到最后。"
    taku "所以……你能不能别一个人生闷气了。"
    taku "我们是真的需要你。你对我们小组来说，绝对不能缺。"

    narrator "风从三个人之间吹过去。天色已经很暗了，远处教学楼一盏一盏亮起灯。"

    show suzu thinking at right2
    suzu "……我也有问题吧。"
    suzu "Taku 说得也不是全错。我确实总是太想把边界收得很死。"
    suzu "有时候，连别人想保留下来的东西为什么重要，都没先认真听完。"

    show taku neutral at center
    taku "那我们重新听不就好了。"

    show haru smile at left2
    haru "好啦。既然两边都开始反省了，那是不是差不多可以停在这里了？"
    taku "组长发话了。"

    show suzu smile at right2
    suzu "……嗯。"
    narrator "这次，他真的很轻地笑了一下。虽然只有一点点，但已经足够让我和 Taku 同时松口气了。"

    hide haru
    hide taku
    hide suzu
    with dissolve

    # ---------------------------------
    # 场景十一：热可可
    # ---------------------------------
    scene bg teaching_building_corridor_dusk with Dissolve(0.8)

    narrator "和 Suzu、Taku 分开以后，我先回了一趟讨论室拿东西。"
    play music "bgm/huanghun.mp3" volume 0.3 fadeout 1.0 fadein 1.0
    narrator "教学楼里已经很安静了，大部分教室都熄了灯，只有走廊上的灯还亮着，把地面照得发白。"
    narrator "等一整天的紧绷慢慢退下去以后，我才后知后觉地觉得累。"
    narrator "不只是跑来跑去的累，心也被拽着转了一整天，终于停下来时只剩下一种发空的疲惫。"

    scene bg meeting_room_evening with Dissolve(0.8)

    show saku neutral at right1, chara_enter_right
    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "我推开讨论室的门，然后愣了一下。Saku 居然还在。"
    narrator "她坐在靠门的位置，桌上放着一个纸杯，旁边还有她没收起来的平板。"

    saku "回来了。"
    haru "……你怎么还没走？"
    saku "……等你呗。"

    narrator "我的动作顿了一下。"
    narrator "她把桌上的纸杯往我这边推了推，淡淡的可可香一下子飘过来，还带着一点热气。"

    saku "快喝吧。不然要凉了。"
    haru "这是……给我的？"
    saku "嗯。你今天看起来很累。"

    narrator "我低头看着那杯热可可，忽然有点说不出话。"
    narrator "明明只是很普通的一杯热饮，可在这种时候，被人这样安静地留着等你，好像连心里那些发酸发紧的地方都会一起被捂热一点。"

    haru "谢谢。"
    narrator "我捧起纸杯，掌心一下子暖起来。"

    saku "你总是那个去安慰别人的人。"
    haru "……有吗？"
    saku "有。谁不说话了，你会去找。谁看起来不对劲，你也会去看。明明自己也会累。"

    narrator "我怔了两秒，忽然有点想笑，又有点鼻子发酸。"
    haru "原来你有发现啊。"
    saku "……这是个人都能看出来吧。"
    narrator "我笑出了声。她还是那种说话方式，可那种笨拙又直接的关心，反而让人觉得很真实。"
    saku "所以，偶尔也轮到别人管一下你吧。"

    narrator "走廊外很安静。夜风从没关紧的窗缝里吹进来，把桌上的纸轻轻掀起一点边角。"
    narrator "我捧着热可可，站在原地看着她，忽然觉得今天那些乱七八糟的事情，好像终于在这一刻有了一个能让人慢慢呼气的落点。"

    hide saku
    hide haru
    with dissolve

    scene bg black with Dissolve(1.0)
    stop music fadeout 5.0

    # ---------------------------------
    # 场景十二：还没有结束的风
    # ---------------------------------
    narrator "事情并没有因此就全部解决。"
    narrator "进度还是紧，老师的提醒还在，要做的东西也一点没少。"
    narrator "我们明天依然得继续开会，继续赶工，继续在“想做得更好”和“必须来得及做完”之间找平衡。"
    narrator "可和昨天不一样的是，至少今晚，没人再一个人站在原地了。"
    narrator "风开始变急。"
    narrator "可我们也终于不是各自散开的纸。"

    call show_chapter_end_card("第三章", "风平浪静之后") from _call_show_chapter_end_card_ch3

    return
