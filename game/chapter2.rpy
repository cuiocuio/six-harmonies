# =========================================
# chapter2.rpy
# 《Six Harmonies》第二章：放学后的草稿纸
# =========================================
#
# 建议新增背景素材：
# 1. images/bg/teaching_building_corridor_day.png
# 2. images/bg/dessert_shop_afternoon.png
# 3. images/bg/arcade_mall_afternoon.png
# 4. images/bg/teaching_building_corridor_dusk.png
# 5. images/bg/rooftop_dusk.png
# 6. images/bg/campus_path_dusk.png
#
# 建议新增CG/演出素材（可选）：
# 1. images/cg/saku_character_sheet.png
# 2. images/cg/hina_script_pages.png
# 3. images/cg/rei_arcade_closeup.png
# 4. images/cg/suzu_night_meeting.png
#
label chapter_2:

    scene bg black
    with fade


    # ---------------------------------
    # 场景零：课后邀约
    # ---------------------------------
    scene bg classroom_xigai
    with fade

    narrator "上午"
    narrator "又是无聊的习概课，我在教室里玩了一上午的手机，头晕眼花的"
    narrator "终于听到了下课铃，我习惯性慢悠悠地走出教室"

    scene bg teaching_building_corridor_day
    with dissolve

    show hina neutral at right1, chara_enter_right
    with dissolve

    narrator "在门口，我看到了一个熟悉的身影"
    narrator "是Hina，她站在走廊边上，手里抱着书，看起来像是在等人"
    narrator "我走出来的时候，她还往这边看了一眼"

    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "……欸？她是在等我吗？"

    haru "中午好呀"

    narrator "我率先走过去打了招呼"

    show hina shy at right1
    hina "啊，是Haru"
    hina "我刚好想找你呢……下午有时间吗？"
    hina "如果可以的话，我们可以一起去万象城喝咖啡吗？那家咖啡店的甜品很好吃……"

    narrator "她说到后面的时候，声音还是一如既往地轻"
    narrator "像是怕自己说得太突然，会让我觉得为难一样"
    narrator "不过老实说，我确实愣了一下"
    narrator "Hina主动来约我，这件事本身就已经够让我意外了"
    narrator "更别说还是去喝咖啡"

    show haru serious at left1
    haru "有啊，当然有"

    narrator "我答应得很快，快到我自己都觉得惊讶"

    show haru thinking at left1
    haru "不过，你怎么突然想到约我去喝咖啡呀？"

    narrator "Hina轻轻把耳边的头发别到耳后，有些不好意思地看了我一眼"

    show hina serious at right1
    hina "就是……想跟你聊聊剧本的事"
    hina "而且，最近一直都在开会，好像很久没有这样单独和谁说说话了"

    narrator "她说得很自然"
    narrator "但不知道为什么，这个说法听起来莫名有点让人在意"

    show haru neutral at left1
    haru "好啊，那下午几点？"

    show hina neutral at right1
    hina "两点半可以吗？"
    hina "那时候人应该不会太多"

    haru "行，那我到时候过去找你"

    narrator "Hina点点头，像是终于松了口气"

    show hina shy at right1
    hina "嗯，那下午见"

    narrator "她说完，朝我挥了挥手，就顺着楼梯往另一边走了"
    narrator "……奇怪"
    narrator "明明只是约着去喝个咖啡而已，为什么我突然有种像是被安排了什么重要行程一样的感觉"

    hide haru
    hide hina
    with dissolve

    # ---------------------------------
    # 场景一：甜品店里，Hina说了很多话
    # ---------------------------------
    scene bg dessert_shop_afternoon
    with fade

    show hina neutral at right1, chara_enter_right
    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "下午，万象城"
    narrator "商场里冷气开得很足，从自动门进去的一瞬间，好舒服……"
    narrator "我有种重新活过来的感觉"
    narrator "暑气被隔绝在外面，耳边只剩下商场里循环播放的背景音乐，还有路过的人群说话声"
    narrator "我照着Hina发来的位置，坐扶梯上了三楼，很快就在角落里看见了她"
    narrator "她已经到了，坐在靠窗的位置，桌上放着两杯水，面前还摆着一本小小的便签本"

    hina "这里"

    haru "来这么早呀"

    show hina shy at right1
    hina "嗯。我也才刚到没多久……"

    narrator "不，这一看就已经坐下至少十分钟了吧"
    narrator "不过我没拆穿她，只是在她对面坐了下来，顺便看了一眼菜单"
    narrator "店里装修得很干净，桌子是偏浅色的木纹，窗边还摆了一排绿植"
    narrator "空气里全是甜甜的奶油香味，旁边柜台里的蛋糕一个比一个长得过分精致"

    show haru troubled at left1
    narrator "……糟糕，感觉钱包有点危险"

    narrator "Hina像是看出了我正在心里偷偷计算价格，轻轻笑了一下"

    show hina neutral at right1
    hina "这家虽然看起来有点贵，不过甜品真的很好吃"
    hina "我请你也可以的"

    haru "那不行，这也太丢脸了吧"

    narrator "我立刻坐直了"
    narrator "请客什么的，还是算了"
    narrator "至少在这种场合不行"
    narrator "最后我们一人点了一杯咖啡，另外又分着点了一份草莓千层和一份焦糖布丁"
    narrator "等待上餐的空隙里，我们之间短暂地安静了一会"
    narrator "不过，那种安静并不尴尬"
    narrator "外头商场里熙熙攘攘的声音把空白都填满了，即使没说话，也不会觉得别扭"

    show haru neutral at left1
    haru "所以，你今天特地找我，是想聊剧本吗？"

    show hina serious at right1
    hina "嗯……也不只是剧本吧"

    narrator "她低头看着杯子里的水，指尖轻轻碰了一下杯沿"

    hina "我最近一直在想，我们定下来的那个方向"
    hina "就是……“六个人一起做一款游戏”这个故事"

    haru "嗯"

    hina "我觉得它很好"
    hina "不是那种很夸张、一下子就很厉害的点子，但越想越觉得，里面有很多可以写的东西"

    narrator "她说这些话的时候，眼神一点点认真起来"
    narrator "和平时那种轻轻柔柔的感觉不太一样"
    narrator "像是终于谈到了她真正很在意的部分"

    hina "比如，一个人表面上看起来很凶，其实会在大家看不到的地方照顾人"
    hina "比如，一个人看起来总是很不正经，可气氛冷掉的时候，反而是他第一个跳出来接话"
    hina "还有……明明很会安排事情的人，也会偷偷一个人去天台透气"

    narrator "……等等"
    narrator "这个“比如”，是不是有点太精准了"

    show haru thinking at left1
    haru "你已经开始偷偷观察大家了啊"

    narrator "Hina愣了一下，似乎是因为被我看穿了而有点不好意思"

    show hina shy at right1
    hina "也、也没有偷偷……"
    hina "只是，大家都很有自己的特点，很容易就会注意到"

    narrator "她越解释越可疑了"
    narrator "不过我没继续逗她"
    narrator "刚好这个时候甜品也送上来了，草莓千层被切得整整齐齐，奶油上的草莓看起来鲜红得像精修图"
    narrator "我尝了一口"

    show haru serious at left1
    haru "……好好吃"

    show hina neutral at right1
    hina "对吧"

    narrator "她像是有点得意，轻轻的得意，像小猫尾巴晃了一下"

    hina "因为我之前和室友来过一次"
    hina "那时候就觉得，如果以后有机会的话，还想带朋友一起来"

    narrator "朋友啊"
    narrator "虽然只是很普通的说法，但从她嘴里说出来，还是有种很微妙的感觉"
    narrator "商场窗外的光落在桌子边上，把杯子里的冰块都照得有点亮"
    narrator "甜品吃到一半的时候，话题也慢慢从剧本扯到了别的地方"
    narrator "比如上课无聊的时候她会在本子角落里画一些乱七八糟的小图案"
    narrator "比如她其实不太擅长拒绝别人，所以经常会因为一些莫名其妙的理由接下额外的事"
    narrator "再比如她其实很喜欢那种老式的恋爱电影，看到太俗套的桥段也会认真跟着心动一下"
    narrator "我一边听，一边偶尔接话"
    narrator "也不知道是不是因为店里的环境太舒服了，还是因为Hina说话的方式本来就很容易让人放松，不知不觉间，时间就过去了很久"

    show hina troubled at right1
    hina "啊，都这个时间了……"

    narrator "她低头看了一眼手机，语气里带着一点惊讶"
    narrator "我也跟着看了眼时间"
    narrator "居然已经快四点了"
    narrator "……不是，我们到底聊了多久啊"

    show haru neutral at left1
    haru "感觉时间过得也太快了"

    show hina shy at right1
    hina "嗯……本来还以为，可能只坐一会就回去了"
    hina "不过，今天聊得很开心"

    narrator "其实我也这么想，很久没有和人说过这么多话了"

    haru "那下次还可以再来"

    narrator "Hina看着我，嘴角微微弯了起来"

    hina "好呀"

    hide haru
    hide hina
    with dissolve

    # ---------------------------------
    # 场景二：电玩城里，正在打舞萌的Rei
    # ---------------------------------
    scene bg arcade_mall_afternoon
    with fade

    show hina neutral at right1, chara_enter_right
    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "从甜品店出来以后，商场里的人明显比刚才更多了些"
    narrator "我和Hina慢慢往外走，路过电玩城门口的时候，里面传来了十分富有节奏感的拍打声"
    play music "bgm/yinyou.mp3" volume 0.5 fadeout 1.0 fadein 1.0
    narrator "我下意识往里看了一眼"
    narrator "是舞萌DX，一种长得像洗衣机一样的街机音游。每次路过都有一堆人玩"
    narrator "真不理解这种拍拍机有什么好玩的"
    narrator "突然，我看到屏幕前站着一个非常眼熟的身影"
    narrator "黑色茂密的头发，手臂抬起又落下，动作熟练得几乎不带停顿"
    narrator "……是Rei"

    haru "等等，那不是Rei吗？"

    show hina serious at right1
    hina "真的诶……"

    narrator "舞萌机台前围了几个人，屏幕上的光不停跳动，音效也快得让人眼花"
    narrator "Rei站在机子前，神情难得地专注，动作利落得像根本没经过思考一样"
    narrator "我们盯着他看了将近一分钟，他居然毫无察觉"
    narrator "终于，机器上传来结算音效"
    narrator "Rei打得大汗淋漓，甩了甩手，像是准备去打下一首，一转头就看见了我们"

    hide haru
    hide hina
    show rei neutral at center, chara_enter_fade
    with dissolve

    narrator "他愣住了"

    show rei annoyed at center
    rei "……你，你们怎么在这"

    narrator "他尴尬地挠了挠头，眼睛不知道该看哪才好"

    show haru thinking at left2
    haru "这话应该我问你吧"
    haru "没想到你居然爱玩拍拍机"

    rei "……一般宅男哥出门不都喜欢玩这个"

    narrator "……"
    narrator "怎么还有人自称宅男哥啊！"

    show haru neutral at left2
    haru "你玩这个很厉害啊"

    show rei serious at center
    rei "这本来就不难"

    narrator "……可恶，好装"
    narrator "但偏偏他说这话的时候表情又很平，搞得像真的只是在陈述事实一样，连吐槽都不好吐槽"

    narrator "Hina站在我旁边，犹豫了两秒，小声开口"

    show hina shy at right2
    hina "Rei同学，你好厉害"
    hina "我刚才看的眼睛都花了，你居然能全部连上"

    narrator "Rei看了她一眼，沉默了半秒"

    rei "还行吧"

    narrator "我又差点没绷住"
    narrator "这个人，嘴上说着“还行”，脸上却写着“别大惊小怪”"
    narrator "真是某种意义上的很好懂"

    haru "你一个人来的？"

    rei "嗯"
    rei "写程序写累了，会来打两首"

    narrator "……这句话，倒是有点出乎我意料"
    narrator "我还以为Rei这种人，放松方式应该是回寝室关灯睡觉，或者把所有人屏蔽以后安静地待着"
    narrator "没想到居然是来电玩城打音游"

    haru "还挺适合你的"

    rei "什么意思"

    haru "就是，看起来很像你会擅长的东西"
    haru "节奏准、反应快，还不太需要社交"

    show rei annoyed at center
    rei "……最后一句可以删掉"

    narrator "很好，看来他自己也知道"
    narrator "旁边又有人等着上机，Rei看了眼时间，把卡收了起来"

    show haru neutral at left2
    haru "今天晚上还有会议哦，可别玩太久了"

    show rei serious at center
    rei "我知道"

    show hina neutral at right2
    hina "那……晚上见"

    rei "嗯"

    narrator "我们和Rei在电玩城门口分开，继续往商场外走"

    hide haru
    hide hina
    hide rei
    with dissolve

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景三：Saku带来的人设初稿
    # ---------------------------------
    scene bg meeting_room_evening with Dissolve(0.8)

    show taku smile at left2, chara_enter_left
    show suzu serious at left1, chara_enter_left
    hide suzu
    show haru neutral at center, chara_enter_fade
    show rei neutral at right2, chara_enter_right
    hide rei
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "晚上，教学楼讨论室"
    play music "bgm/cafe.mp3" volume 0.5 fadeout 1.0 fadein 1.0
    narrator "等我到的时候，其他人已经差不多都到了"
    narrator "Taku正靠在椅子上转笔，一副“我今天状态很好快让我发言”的样子"
    narrator "Suzu坐在靠窗的位置，笔记本电脑已经打开"
    narrator "Rei来得比我想象中还早，看样子电玩城那边没待多久"
    narrator "而Saku，则把平板放在桌面上，安安静静地坐在那儿"
    narrator "不知是不是我的错觉"
    narrator "今天的她，看起来和平时有点不一样"
    narrator "虽然表情还是淡淡的，但能看出来，她似乎早就准备好了什么"

    show saku serious at right2
    narrator "我刚坐下，Saku就抬眼看了我们一圈"

    saku "我把每个人的初步形象设计了一下"

    narrator "……哇"
    narrator "她居然第一个讲话了"

    show taku excited at left2
    taku "真的假的？这么快？！"

    narrator "Saku只是低头点开平板，把第一张图放了出来"
    narrator "屏幕上的人物线条还带着草稿感，配色也不算完全定下来，但那种“这个人真的已经站在面前了”的感觉，已经非常清楚了"
    narrator "第一个是偏温柔安静类型的女孩子，长发，眼神柔和，校服上还做了很细的设计"
    narrator "第二个是看起来元气但不至于太闹腾的男生"
    narrator "第三个则明显更偏冷一点，轮廓利落，神情淡淡的"
    narrator "她一个一个往下翻"
    narrator "每翻一张，桌边就会安静一会"
    narrator "是因为真的画得很好啊"
    narrator "而且，每个形象似乎都可以看到我们本人的影子"

    hide suzu
    with dissolve

    hide taku
    show hina shy at left2, chara_enter_left
    with dissolve

    hina "……好漂亮"

    hide hina
    show taku excited at left2
    taku "太强了吧？！"
    taku "这已经完全能想象他们在故事里讲话的样子了！"
    taku "还有啊，没想到我的二次元形象这么帅啊哈哈哈哈哈"

    hide saku
    show rei serious at right2
    rei "不错，这个程序员画得很有死宅味，但很帅"
    rei "简直就是我（）"

    hide taku
    show suzu serious at left2, chara_enter_left
    with dissolve

    suzu "配色也很统一"
    suzu "整体风格比我想象中的更稳"

    narrator "就连Suzu都给出这种评价了，说明是真的很满意"
    narrator "我仔细地看了看Saku为我画的草图，一个很可爱的长发女孩，穿着JKS，带着一个小猫发夹，而这个发夹正是我天天挂在书包上的"

    show haru serious at center
    haru "好可爱……"
    haru "这个JK也太萌了吧"

    narrator "我情不自禁地发出了感慨"

    hide rei
    show saku neutral at right2
    saku "我觉得还挺适合你的"

    narrator "Saku小声说着，没有看我"
    narrator "我看着Saku平板上的那些草图，心里忽然有种特别实在的感觉"
    narrator "像我们之前一直挂在嘴边的“做一部游戏”，终于不是停留在白板上的几个字了"
    narrator "它真的开始长出形状了"

    hide suzu
    show taku smile at left2
    taku "太厉害了吧，Saku"
    taku "你简直太可靠了"

    narrator "她停了一下，移开视线"

    show saku annoyed at right2
    saku "这只是初稿而已"
    saku "后面还会改进的"

    narrator "虽然语气还是那样，轻描淡写的"
    narrator "但我能感觉到，她好像有一点点开心"
    narrator "Taku已经兴奋得不行了，指着其中一张图开始胡说八道"

    taku "欸，这个一看就是那种第一眼很难接近，但后面会偷偷给你带热饮的类型！"
    taku "这个看起来就是傲娇型！"

    saku "……我才没设定这种东西"

    taku "现在不就有了吗"

    narrator "……这家伙，已经开始给人设强行加戏了"
    narrator "不过大家的心情明显都很好"
    narrator "我们围着那几张初稿聊了很久，从发色、制服细节，到人物站姿、神态、立绘上该保留哪些小习惯，甚至连“这个角色讲话时会不会习惯性别开视线”这种细节都认真讨论了一轮"
    narrator "那场会一直开到不算早"
    narrator "散会的时候，我脑子还是热的"
    narrator "可能是因为太久没有这种“每个人都在为同一个东西高兴起来”的感觉了"

    hide taku
    hide suzu
    hide haru
    hide hina
    hide rei
    hide saku
    with dissolve

    # ---------------------------------
    # 场景四：Hina，写出了开头
    # ---------------------------------
    scene bg dorm_room_day
    with fade

    show haru neutral at center, chara_enter_fade
    with dissolve

    narrator "第二天下午"
    play music "bgm/shitang.mp3" volume 0.15 fadeout 1.0 fadein 1.0
    narrator "我正坐在宿舍里发呆，手机突然震了一下"
    narrator "是群消息"

    show hina shy at left2, chara_enter_left
    with dissolve

    hina "那个……大家现在方便吗？"
    hina "我昨晚突然很有灵感，把前面的剧本写了一部分。想给大家看看……"

    narrator "我一下子坐直了"
    narrator "不只是我，群里其他人也反应得很快"

    hide hina
    show taku excited at left2, chara_enter_left
    with dissolve

    taku "哇靠，这么快？！"

    hide taku
    with dissolve

    show rei serious at left2, chara_enter_left
    with dissolve

    rei "发"

    hide rei
    with dissolve

    show suzu serious at right2, chara_enter_right
    with dissolve

    suzu "如果需要当面讨论的话，我现在可以过去"

    hide suzu
    with dissolve

    show saku neutral at right2, chara_enter_right
    with dissolve

    saku "我也可以"

    narrator "这个群，终于开始像个真正的小组群了"

    show haru serious at center
    haru "那还是老地方吧，半小时后见？"

    show hina neutral at left2
    hina "好"

    hide haru
    hide hina
    hide saku
    with dissolve

    # ---------------------------------
    # 场景五：会议室里的剧本试读
    # ---------------------------------
    scene bg meeting_room_day
    with fade

    show taku smile at left2, chara_enter_left
    show hina troubled at left1, chara_enter_left
    hide hina
    show haru neutral at center, chara_enter_fade
    show rei neutral at right2, chara_enter_right
    hide rei
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "讨论室"
    narrator "Hina坐在桌边，把打印出来的几页纸小心地放在中间"
    narrator "纸页边缘被她压得整整齐齐，像是来之前还特意重新整理过"
    narrator "她的表情看起来有点紧张"

    hide saku
    show hina shy at right2, chara_enter_right
    hina "不过，我只写了前面的一部分……可能还有很多地方要改"

    taku "别怕，我们会温柔的"

    hide taku
    show rei neutral at left2, chara_enter_left
    rei "你先把你嘴闭上，就是最大的温柔"

    narrator "……气氛还是一如既往地稳定"
    narrator "我把剧本拿过来看了两眼"
    narrator "开头写得很顺"
    narrator "它没急着把所有设定一口气塞进去，只是很自然地从几个人的第一次碰面、彼此的第一印象，还有会议时那种微妙的生疏感切进去"
    narrator "有点安静，但不无聊"
    narrator "而且，有一种很难形容的“像我们，但又不是完全照搬我们”的感觉"

    show haru serious at center
    haru "这个开头很好啊"

    narrator "Hina微微睁大眼睛，看起来像是松了一点气"

    hide taku
    hide rei
    show hina shy at left2
    hina "真的吗？"

    haru "真的"
    haru "而且读起来很顺，不会让人觉得硬"

    hide hina
    show taku excited at left2
    taku "来来来，光看多没意思，我们读一下吧"
    taku "试读，必须试读"

    narrator "……这人一开口，我就有种不祥的预感"
    narrator "但不知道为什么，其他人居然也都没反对"
    narrator "于是几分钟后，我们就真的开始了非常草率但异常投入的剧本试读"
    narrator "Taku抢了最显眼的那句台词，一张口就用那种极其夸张、像深夜狗血校园剧男主角一样的语调念了出来"
    play music "bgm/huaji.mp3" volume 0.5 fadeout 1.0 fadein 1.0

    taku "——你以为，只要把文件发到群里，就算是合作了吗？！"

    narrator "Hina第一个没忍住，低下头笑出了声"

    hide taku
    show hina serious at left2
    hina "才不是这样的啊喂！"

    narrator "我也绷不住了"

    show haru neutral at center
    haru "什么啊！"
    haru "谁会这么讲话啊？！"

    hide saku
    show rei annoyed at right2
    rei "你把一个正常角色读成了脑子有问题的人"

    hide rei
    show saku annoyed at right2
    saku "……太吵了"

    narrator "但她说这句话的时候，嘴角也分明动了一下"

    hide saku
    with dissolve

    show suzu thinking at right2, chara_enter_right
    with dissolve

    narrator "连Suzu都抬手按了按额角，像是在忍笑"

    hide hina
    show taku smile at left2
    taku "不是，我这是在帮你们测试台词有没有表演张力！"

    haru "你的表演张力太超前了，我们暂时消化不了"

    narrator "接下来十几分钟，会议室里简直乱成一团"
    narrator "我们轮流读台词，有人读得太平，有人故意读得太夸张"
    narrator "有一句“那今天先到这里吧”甚至被Taku硬生生读出了“诀别现场”的感觉"
    narrator "不过，在这种乱七八糟的试读里，很多问题反而真的看出来了"
    narrator "比如有些句子写得太书面，一念出来就显得不自然"
    narrator "有些地方虽然单看没问题，但接在前一句后面会有点突兀"
    narrator "还有一些地方，本来只觉得“还行”，结果一读出来，反而特别有画面"
    narrator "Hina一边听一边飞快记笔记"
    narrator "我忽然觉得，这种感觉其实很奇妙"
    narrator "大家围在一起，笑着闹着，把一份还不算完整的东西一点点磨出样子来"

    # ---------------------------------
    # 场景六：去拍背景素材吧
    # ---------------------------------
    show taku excited at left2
    narrator "试读到一半的时候，Taku突然把笔一拍，像是脑袋里又有什么东西炸开了"

    taku "等等"

    haru "你又怎么了？"

    taku "我们不是正好要做校园背景吗？"
    taku "既然故事本来就在学校里，那干嘛不直接去拍素材？"

    narrator "这句话一出来，大家都愣了一下"

    taku "真的，我觉得这个靠谱"
    taku "教学楼、走廊、天台、操场、林荫路、花园，还有食堂外面的台阶，这些地方不都能直接参考吗？"
    taku "与其坐在这里想，不如出去逛一圈"

    show suzu serious at right2
    suzu "……从效率上讲，可行"

    hide suzu
    show rei serious at right2
    rei "顺便还能决定哪些场景用得上"

    hide suzu
    with dissolve

    hide rei
    show saku neutral at right2
    saku "如果要画背景，有真实参考会轻松很多"

    hide taku
    show hina serious at left2
    hina "而且……说不定还能想到更多细节"

    narrator "居然没有一个人反对"

    show haru serious at center
    haru "那还等什么？"
    haru "走吧"

    call screen timed_choice(
        "Taku提议现在就去拍素材。你会怎么安排？",
        [
            ("立刻出发，趁着黄昏光线取材。", "go_now"),
            ("先补完室内讨论，再统一出发。", "discuss_first"),
        ],
        timeout=6.0,
        timeout_value="timeout"
    )
    $ chapter2_choice = _return

    if chapter2_choice == "go_now":
        $ team_cohesion_score += 1
        narrator "我拍板先出发，大家都迅速收拾好设备往外走。"
        haru "先把光线抓住，边走边补细节。"
    elif chapter2_choice == "discuss_first":
        narrator "我提议先把室内讨论收个尾，再按清单出发。"
        narrator "大家花了几分钟统一分工，然后一起起身。"
    else:
        $ team_cohesion_score -= 1
        narrator "我一时没接上话，短暂的沉默让气氛有点卡住。"
        narrator "最后还是Taku先打破沉默，大家才匆匆出门。"

    hide taku
    hide hina
    hide haru
    hide rei
    hide saku
    hide suzu
    with dissolve

    scene bg black with Dissolve(0.8)

    # ---------------------------------
    # 场景七：校园黄昏，大家一起闲逛
    # ---------------------------------
    scene bg teaching_building_corridor_dusk with Dissolve(0.8)

    show taku excited at left2, chara_enter_left
    show rei neutral at left1, chara_enter_left
    hide rei
    show haru neutral at center, chara_enter_fade
    show hina neutral at right2, chara_enter_right
    with dissolve

    narrator "傍晚，校园里"
    play music "bgm/huanghun.mp3" volume 0.3 fadeout 1.0 fadein 1.0
    narrator "从教学楼出来的时候，太阳已经慢慢往西边落了"
    narrator "风也比白天舒服很多，吹在脸上不再是那种闷热的感觉"
    narrator "Taku拿着手机，自告奋勇充当“素材摄影师”，一边走一边嚷嚷“这个角度绝了”“这个树影超有gal感”"
    narrator "Rei跟在旁边，时不时冷冷补一句“你拍歪了”"
    narrator "这两个人凑在一起，真是某种意义上的灾难与平衡"
    narrator "我们先去了教学楼前那条长走廊"
    narrator "傍晚的光从窗户斜斜照进来，把地面切成一块一块很规整的亮色"

    hina "这个地方很适合写第一次认真对话的场景"

    scene bg rooftop_dusk
    with fade

    show taku excited at left2
    show rei neutral at left1
    hide rei
    show haru neutral at center
    show hina neutral at right2
    hide hina
    show saku neutral at right2
    with dissolve

    narrator "然后是天台"
    narrator "风比楼下大得多，夕阳把栏杆都染成了橙金色"

    hide saku
    with dissolve

    show suzu serious at right2, chara_enter_right
    with dissolve

    narrator "Suzu难得没有立刻说“这里不安全”，只是站在旁边看了一会，然后提醒Taku别把手机探出去太多"

    scene bg campus_path_dusk
    with fade

    show taku excited at left2
    show rei neutral at left1
    hide rei
    show haru neutral at center
    show hina neutral at right2
    hide hina
    show suzu serious at right2
    with dissolve

    narrator "接着是操场边、图书馆前，还有教四后面的小花园"

    scene bg garden_dusk
    with fade

    show taku excited at left2
    show rei annoyed at left1
    hide rei
    show haru neutral at center
    show hina neutral at right2
    hide hina
    show saku neutral at right2, chara_enter_right
    with dissolve

    narrator "走到花园的时候，泡芙居然真的又出现了"

    taku "哇，这就是传说中的隐藏NPC？"

    saku "……它不是NPC"

    narrator "她蹲下来，把包里不知道什么时候带着的猫条拿出来"
    narrator "泡芙果然先朝她靠了过去"

    taku "欸，我也来试试"

    narrator "Taku还想靠近，被泡芙非常不给面子地躲开了"

    hide saku
    show rei annoyed at right2, chara_enter_right
    rei "看吧，不是所有生物都会喜欢你"

    taku "不是，它对我有偏见"

    haru "可能是你话太多了"

    narrator "我们几个人站在花园边上，看着夕阳一点点落下去"
    narrator "树影被拉得很长，风吹过的时候，叶子会发出很轻很轻的响声"
    narrator "不知道是谁先笑了一声，接着大家就都慢慢聊开了"
    narrator "聊剧情，聊上课，聊食堂今天的菜有多难吃，聊如果真的把这个故事做出来，最先被吐槽的到底会是剧本还是程序"
    narrator "在第一周刚开始的时候，我根本想象不到，会有这样一个傍晚"
    narrator "大家什么都没急着赶，也没谁急着要离开"
    narrator "只是一起在校园里慢慢走，看到觉得合适的地方就停下来拍两张，顺便说几句没什么意义但会让人忍不住想笑的话"
    narrator "很普通"
    narrator "也正因为普通，才让人觉得舒服"
    narrator "那些原本“为了完成任务才被绑在一起”的别扭感，也在傍晚的光里悄悄化开了一点"

    hide taku
    hide rei
    hide haru
    hide hina
    hide saku
    hide suzu
    with dissolve

    scene bg black with Dissolve(1.0)

    # ---------------------------------
    # 场景八：深夜的会议室，还亮着灯
    # ---------------------------------
    scene bg dorm_room_day with Dissolve(1.0)

    show haru thinking at center, chara_enter_fade
    with dissolve

    narrator "晚上十一点，宿舍"
    narrator "我坐在桌前，正准备把今天会议和试读的内容整理一下发进群里，结果一低头，突然发现我的记事本不见了"
    narrator "我把桌上翻了一遍，书包也翻了一遍，最后不得不承认一个现实"
    narrator "……大概率是落在讨论室了"
    narrator "都这个点了，我是真的很不想再跑一趟"
    narrator "可如果不去拿，明天我多半又要忘"
    narrator "我叹了口气，认命地套上外套，慢吞吞地下楼往教学楼走"

    scene bg campus_path_dusk
    with fade

    narrator "夜里的校园安静得很，路灯把地面照得一块亮一块暗"
    narrator "远处还能听见操场那边传来一点模糊的人声"
    narrator "我走到讨论室门口的时候，刚想直接推门"
    narrator "里面还亮着灯"
    narrator "……这么晚了，谁还在？"

    scene bg meeting_room_evening
    with fade

    show suzu thinking at right1, chara_enter_right
    show haru neutral at left1, chara_enter_left
    with dissolve

    narrator "我轻轻推开门"
    narrator "门内，Suzu正坐在桌边，电脑屏幕亮着，旁边摊了几页打印出来的剧本，桌角还放着两罐已经空了的咖啡"
    narrator "他听见动静，抬头看向我"

    suzu "你怎么来了？"

    haru "我记事本落这了"
    haru "你才是，怎么还没回去？"

    narrator "我一边说，一边走进去，果然在桌上找到了自己的本子"
    narrator "但视线很快又被他桌上的东西吸引了过去"
    narrator "浏览器开了好几个标签页，标题几乎全和galgame有关"
    narrator "什么“经典galgame叙事结构”“AVG脚本演出方式”“常见UI设计逻辑”“校园恋爱文字游戏节奏控制”之类的，看得我眼花缭乱"

    show haru thinking at left1
    haru "你……在查这些？"

    narrator "Suzu把眼镜往上推了一下，声音里带着一点很轻的疲惫"

    suzu "嗯"
    suzu "我以前没怎么玩过galgame"
    suzu "今天听你们试读之后，觉得自己对这个类型还是了解得不够"
    suzu "所以想先补一点相关的东西，再顺便把Hina的剧本按大家今天提的意见整理一下，看看结构还能怎么调整"

    narrator "他说得很平静，像是在说一件再普通不过的事"
    narrator "可我看着那两罐空掉的咖啡，再看看他明显有些发青的眼下，怎么都没法把这事归类成“普通”"

    show haru serious at left1
    haru "你这样也太拼了吧"

    show suzu serious at right1
    suzu "还好"

    narrator "不，这看起来一点都不像“还好”"
    narrator "我走到他旁边，看了一眼屏幕上密密麻麻的笔记"
    narrator "上面甚至已经分好了几栏"
    narrator "开头节奏调整"
    narrator "角色出场顺序"
    narrator "可视化演出建议"
    narrator "后续分支预留"
    narrator "工期可行性"
    narrator "……这家伙，似乎想把所有东西都往自己身上拢了"

    haru "其实，你不用什么都自己扛着"

    narrator "Suzu敲键盘的手停了一下"
    narrator "他没立刻看我，只是盯着屏幕，过了几秒才开口"

    suzu "我只是希望，我们的项目能做得更好一点"

    haru "可这本来就不是你一个人的项目啊"
    haru "大家都在做事，真的没必要把所有东西都揽到自己身上"

    narrator "我说完以后，房间里安静了两秒"
    narrator "窗外夜色很深，只有走廊上的灯从玻璃门外映进来一点"

    narrator "Suzu终于轻轻呼了口气，靠在椅背上"

    show suzu thinking at right1
    suzu "我知道"
    suzu "只是……如果我能先多处理一些，后面你们就会少很多麻烦"

    haru "你怎么老想着“不给别人添麻烦”啊"

    suzu "因为麻烦本来就没必要增加"

    narrator "……这句话，说得还真像他"
    narrator "我看着他，突然又想起第一次在天台上遇到他的时候"
    narrator "他说自己压力大的时候会来透气"
    narrator "可现在看来，他根本不是会乖乖去透气的类型"
    narrator "他是那种明明已经很累了，却还是会坐在原地，把事情一项项继续做下去的人"

    haru "可你这样的话，反而会让人担心啊"

    narrator "这次，Suzu终于转头看向我"
    narrator "他的神情还是很平静"

    show suzu serious at right1
    suzu "……抱歉"

    haru "这不是道歉的问题吧"
    haru "总之，今天先到这里"
    haru "再这样下去，你明天上课要么睡死，要么直接猝死"

    show suzu neutral at right1
    suzu "没有这么夸张"

    haru "有"
    haru "而且我们又不是摆设"
    haru "剧本的问题可以明天继续一起改，没必要你一个人全做完"

    narrator "他沉默了一会，最后还是把手从键盘上移开了"
    narrator "虽然动作很轻，但我看得出来，他应该是真的累了"

    show suzu thinking at right1
    suzu "……好吧"
    suzu "那我把这个保存一下就走"

    narrator "我总算松了口气"
    narrator "我都怀疑，今晚如果我不来，他会不会直接在这里熬到凌晨两三点"
    narrator "Suzu低头保存文件的时候，我顺手帮他把桌上的纸整理了一下"
    narrator "讨论室里很安静，只剩下风扇和电脑主机运转的声音"
    narrator "不知道为什么"
    narrator "明明只是来拿个记事本，我却忽然觉得，这一晚看到的东西，好像比白天任何一场会都更接近“真正的他”"
    narrator "认真、克制、可靠"
    narrator "但也比想象中更容易把自己逼得太紧"
    narrator "几分钟后，我们一起关掉了讨论室的灯"
    narrator "走廊里的光照下来，把两个人的影子拖得很长"
    narrator "谁都没有再说太多话，只是并肩往楼下走"
    narrator "夜风从门口吹进来，带着一点凉意"
    narrator "我抱着记事本，下意识侧头看了Suzu一眼"
    narrator "他的神情还是和平时差不多，没什么明显的情绪"
    narrator "可那一瞬间，我还是莫名觉得"
    narrator "这个项目，可能真的在一点点把我们每个人原本藏起来的部分，都慢慢照出来"

    hide haru
    hide suzu
    with dissolve

    call show_chapter_end_card("第二章", "放学后的草稿纸") from _call_show_chapter_end_card_ch2

    return
