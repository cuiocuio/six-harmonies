# =========================================
# characters.rpy
# 角色 / 立绘 / 背景 / 站位 / 简单效果
# =========================================

# ---------- 角色定义 ----------
define narrator = Character(None)

define t    = Character("Teacher", color="#000000")
define haru = Character("Haru", color="#000000")
define taku = Character("Taku", color="#000000")
define rei  = Character("Rei",  color="#000000")
define hina = Character("Hina", color="#000000")
define saku = Character("Saku", color="#000000")
define suzu = Character("Suzu", color="#000000")
define student_a = Character("StudentA", color="#000000")
define student_b = Character("StudentB", color="#000000")
define student_c = Character("StudentC", color="#000000")

define subtitle = Character("字幕", color="#000000")


# ---------- 背景 ----------
image bg black = Solid("#000")
image bg classroom_day = "images/bg/classroom_day.png"
image bg classroom_xigai = "images/bg/classroom_xigai.png"
image bg meeting_room_day = "images/bg/meeting_room_day.png"
image bg meeting_room_evening = "images/bg/meeting_room_evening.png"
image bg campus_path_morning = "images/bg/campus_path_morning.png"
image bg campus_path_dusk = "images/bg/campus_path_dusk.png"
image bg garden_afternoon = "images/bg/garden_afternoon.png"
image bg garden_dusk = "images/bg/garden_dusk.png"
image bg dorm_room_day = "images/bg/dorm_room_day.png"
image bg rooftop_afternoon = "images/bg/rooftop_afternoon.png"
image bg rooftop_dusk = "images/bg/rooftop_dusk.png"
image bg canting = "images/bg/canting.png"
image bg dessert_shop_afternoon = "images/bg/dessert_shop_afternoon.png"
image bg arcade_mall_afternoon = "images/bg/arcade_mall_afternoon.png"
image bg teaching_building_corridor_day = "images/bg/teaching_building_corridor_day.png"
image bg teaching_building_corridor_dusk = "images/bg/teaching_building_corridor_dusk.png"
image bg shahu_park_lakeside_day = "images/bg/shahu_park_lakeside_day.png"
image bg shahu_park_path_day = "images/bg/shahu_park_path_day.png"
image bg convenience_store_night = "images/bg/convenience_store_night.png"

# ---------- 角色立绘 ----------

# Haru
image haru neutral  = "images/characters/haru/neutral.png"
image haru thinking = "images/characters/haru/thinking.png"
image haru serious = "images/characters/haru/thinking.png"
image haru troubled = "images/characters/haru/troubled.png"
image haru ganga = "images/characters/haru/ganga.png"
image haru bunaifan = "images/characters/haru/bunaifan.png"
image haru excited = "images/characters/haru/excited.png"
image haru sad = "images/characters/haru/sad.png"
image haru shy = "images/characters/haru/shy.png"
image haru middleshy = "images/characters/haru/middleshy.png"
image haru smile = "images/characters/haru/smile.png"
image haru proud = "images/characters/haru/proud.png"
image haru xmouth = "images/characters/haru/xmouth.png"
image haru surprised = "images/characters/haru/surprised.png"
image haru spark = "images/characters/haru/spark.png"
image haru smileshy = "images/characters/haru/smileshy.png"

# Taku
image taku neutral  = "images/characters/taku/neutral.png"
image taku serious    = "images/characters/taku/serious.png"
image taku smile    = "images/characters/taku/excited.png"
image taku excited  = "images/characters/taku/excited.png"
image taku annoyed  = "images/characters/taku/annoyed.png"

# Rei
image rei neutral   = "images/characters/rei/neutral.png"
image rei serious   = "images/characters/rei/neutral.png"
image rei thinking  = "images/characters/rei/thinking.png"
image rei annoyed   = "images/characters/rei/annoyed.png"
image rei smile     = "images/characters/rei/smile.png"

# Hina
image hina neutral  = "images/characters/hina/neutral.png"
image hina serious = "images/characters/hina/serious.png"
image hina shy = "images/characters/hina/shy.png"
image hina troubled = "images/characters/hina/troubled.png"
image hina cry  = "images/characters/hina/cry.png"
image hina angry = "images/characters/hina/angry.png"
image hina happy = "images/characters/hina/happy.png"
image hina relieved = "images/characters/hina/happy cry.png"
image hina smile = "images/characters/hina/smile.png"
image hina speechless = "images/characters/hina/speechless.png"
image hina fond = "images/characters/hina/proud or care.png"
image hina proud = "images/characters/hina/proud.png"

# Saku
image saku neutral  = "images/characters/saku/neutral.png"
image saku serious  = "images/characters/saku/neutral.png"
image saku shy = "images/characters/saku/shy.png"
image saku annoyed  = "images/characters/saku/annoyed.png"
image saku smile  = "images/characters/saku/smile.png"

# Suzu
image suzu neutral  = "images/characters/suzu/neutral.png"
image suzu serious  = "images/characters/suzu/serious.png"
image suzu thinking = "images/characters/suzu/thinking.png"
image suzu smile    = "images/characters/suzu/smile.png"

# 老师可选
image teacher neutral = "images/characters/teacher/neutral.png"

# ---------- 站位 ----------
# 这是最常用的五个站位
transform left2:
    xalign 0.0
    yalign 1.0

transform left1:
    xalign 0.32
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform right1:
    xalign 0.68
    yalign 1.0

transform right2:
    xalign 1.0
    yalign 1.0

# ---------- 简单入场效果 ----------
transform chara_enter_left:
    xoffset -80
    alpha 0.0
    0.25
    xoffset 0
    alpha 1.0

transform chara_enter_right:
    xoffset 80
    alpha 0.0
    0.25
    xoffset 0
    alpha 1.0

transform chara_enter_fade:
    alpha 0.0
    0.25
    alpha 1.0

# ---------- 当前说话者高亮（可选）----------
# 用法：
# show haru serious at left1
# show taku smile at right1
# 然后对没说话的人加：
# show taku smile at right1, dimmed
transform dimmed:
    matrixcolor BrightnessMatrix(-0.15)

transform normal_light:
    matrixcolor BrightnessMatrix(0.0)
