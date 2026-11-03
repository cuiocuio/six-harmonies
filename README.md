# 六合奏 · Six Harmonies

> A bilingual (中文 / English) narrative visual novel about six people learning to work in harmony, built with [Ren'Py](https://www.renpy.org/).

**Six Harmonies** follows six teammates (Haru, Taku, Rei, Hina, Saku and Suzu) who are thrown together on a project with a hard deadline. They start out disagreeing about almost everything. Over a prologue and four chapters, the player's choices decide whether the six voices become a harmony or fall apart.

---

## Features

- **Branching story with multiple endings.** A hidden *team cohesion* score goes up or down with key decisions. The final chapter checks it and leads to a **Good**, **Neutral** or **Bad** ending.
- **Timed choices.** Some decisions have a countdown timer (`timed_choice` screen). If you hesitate too long, that counts as a choice too.
- **Full bilingual support.** Simplified Chinese is the source language, with a complete English translation (`game/tl/english`). Players pick a language on first launch and can switch at any time.
- **Character staging system.** Five named stage slots (`left2`, `left1`, `center`, `right1`, `right2`) plus enter, fade and dim transforms keep multi-character scenes readable. The speaker is placed at `center` and gets the focus.
- **Custom UI.** Reworked title screen, dialogue box, choice menus, chapter end cards and transitions, with a separate layout for phones and tablets (`game/gui/phone`).
- **Cross-platform.** Builds for Windows / macOS / Linux and Android.

## Architecture

The project is organized into four layers:

| Layer | Responsibility | Where |
|---|---|---|
| **Content** | Story script, branching, game state | `prologue.rpy`, `chapter1–4.rpy`, `script.rpy` |
| **Presentation** | Screens, dialogue UI, choices, transitions, staging | `screens.rpy`, `gui.rpy`, `characters.rpy` |
| **Localization** | Language selection & translations | `i18n.rpy`, `tl/english/` |
| **Assets** | Backgrounds, character sprites, BGM, fonts | `images/`, `bgm/`, `fonts/`, `gui/` |

### Story flow & endings

```
start
 └─ prologue → chapter_1 → chapter_2 → chapter_3 → chapter_4
                              │            │            │
                       team_cohesion_score ± 1 per key (timed) choice
                                                        │
                         ≥ 2 → Good   ·   ≥ 0 → Neutral   ·   < 0 → Bad
```

- The score is declared in `game/script.rpy` (`default team_cohesion_score = 0`) and reset when a new game starts.
- The ending thresholds are evaluated in `game/chapter4.rpy`.

## Project structure

```
.
├── game/
│   ├── script.rpy        # Entry point, global state, chapter sequencing
│   ├── prologue.rpy      # Prologue
│   ├── chapter1-4.rpy    # Main story chapters
│   ├── characters.rpy    # Character definitions, sprites, stage transforms
│   ├── screens.rpy       # UI screens (incl. timed choices)
│   ├── gui.rpy           # GUI configuration
│   ├── options.rpy       # Project / build configuration
│   ├── i18n.rpy          # Language selection & switching
│   ├── tl/english/       # English translation
│   ├── images/           # Backgrounds (bg/) and character sprites (characters/)
│   ├── bgm/              # Background music
│   ├── fonts/            # Fonts
│   └── gui/              # GUI assets (desktop + phone/)
├── android.json          # Android build configuration
├── project.json          # Ren'Py launcher project settings
└── LICENSE
```

## Getting started

1. Install the [Ren'Py SDK](https://www.renpy.org/latest.html) (8.x).
2. Clone this repository into your Ren'Py projects directory:
   ```bash
   git clone https://github.com/cuiocuio/six-harmonies.git
   ```
3. Open the Ren'Py Launcher, select **Six Harmonies**, and click **Launch Project**.

### Building

- **PC (Windows / macOS / Linux):** Launcher → *Build Distributions*.
- **Android:** Launcher → *Android*. Signing keystores are **not** included in this repository. Let the launcher generate new ones, or supply your own (`android.keystore` / `bundle.keystore`, which are git-ignored).

## Tech stack

- **Engine:** Ren'Py 8 (Python-based visual novel engine)
- **Languages:** Ren'Py script, ATL, Python
- **Platforms:** Windows, macOS, Linux, Android

## License

Source code is released under the [Mulan Permissive Software License v2](LICENSE).
Third-party assets (music, fonts) remain under their respective licenses.
