
# sofiakholina-3D-Generation

**Русский** · [English](#english)

**Генерация 3D-модели (без текстуры) по одному или нескольким видам в ComfyUI: 3 workflow + установщик.**

Workflow:

- **3D-Gen_TripoSplat - генерация по одному фото** (точный результат, но с "квадратными" следами на модели)
- **3D-Gen_Trellis - генерация по одному фото** (результат средний, но поверхность гладкая)
- **3D-Gen_Pixal_MV - генерация по 1-4 видам** (результат не слишком хороший, но есть мультивиды)

**Видео по этим Workflow на [YouTube](https://youtu.be/Sw3rYAtZyCk) и [VK](https://vkvideo.ru/video-226908262_456239133)**

**Важно (!) финальные workflow отличаются от показанных в видео**: используйте автоматическую установку по инструкции ниже или обратите внимание на пункт 2 в инструкции внутри workflow, если устанавливаете вручную (добавились ноды).

**Workflow для текстурирования любой вашей 3D-модели:** [sofiakholina-3D-Texturing](https://github.com/sofiakholina/sofiakholina-3D-Texturing).

## Установка

**Только для Windows, видеокарт NVIDIA от 6 GB VRAM с актуальным драйвером и ComfyUI версии 0.45.0 или новее.**

Свободное место на диске: ComfyUI — около 6 GB, модели — около 16 GB для 3-х workflow (можно использовать только один).

### Автоматически

1. Установите ComfyUI: [Comfy Desktop](https://www.comfy.org/download), также подойдёт [ComfyUI Portable](https://github.com/Comfy-Org/ComfyUI/releases).
2. Скачайте этот репозиторий: зелёная кнопка **Code** вверху страницы → **Download ZIP**, распакуйте в любую папку. После успешной установки эту папку можно удалить (для Check.bat и Uninstall.bat скачайте архив заново).
3. Откройте нужный ComfyUI и запустите **Install.bat**, далее установщик задаст вопросы и сделает все сам.

   Если Windows покажет «Система Windows защитила ваш компьютер» — **Подробнее → Выполнить в любом случае**.

4. Workflow находятся в ComfyUI в левой панели **Рабочие процессы** (клавиша W в открытом Comfy).

**Для удаления** откройте нужный ComfyUI и запустите **Uninstall.bat**.

### Вручную

Выполните шаги из [MANUAL_INSTALL.md](MANUAL_INSTALL.md) (они же — в заметке **START** внутри workflow).

## Если не работает

Откройте нужный ComfyUI, запустите **Check.bat** и следуйте инструкциям. Если проблема осталась, найдите файл `diagnostic_report.txt` рядом с Install.bat или по пути из окна проверки, затем отправьте разработчику в [Telegram](https://t.me/sofiakholina).

## Известные особенности

- Если Windows сообщает об отсутствующей VCRUNTIME140.dll или MSVCP140.dll, установите Microsoft Visual C++ Redistributable: https://aka.ms/vc14/vc_redist.x64.exe
- В старом интерфейсе Comfy (не Nodes 2.0) видны служебные настройки Save 3D — их не нужно менять.

## Лицензия

GPL-3.0 (файл LICENSE). Сторонние шаблоны workflow и модели — со своими лицензиями, см. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Ноды s_tools — [sofiakholina-s_tools](https://github.com/sofiakholina/sofiakholina-s_tools).

---

## English

**Generate an untextured 3D model from one or more views in ComfyUI. Includes three workflows and an installer.**

Workflows:

- **3D-Gen_TripoSplat — from one photo** (accurate results, with square marks on the model)
- **3D-Gen_Trellis — from one photo** (fair results, with a smooth surface)
- **3D-Gen_Pixal_MV — from 1–4 views** (limited quality, with support for multiple views)

**Videos about these workflows on [YouTube](https://youtu.be/Sw3rYAtZyCk) and [VK](https://vkvideo.ru/video-226908262_456239133)**

**Important (!) The final workflows differ from those shown in the video:** use the automatic installation instructions below or pay attention to step 2 of the instructions inside the workflow if installing manually (new nodes have been added).

**Workflows for texturing any of your 3D models:** [sofiakholina-3D-Texturing](https://github.com/sofiakholina/sofiakholina-3D-Texturing).

## Install

**Requires Windows, an NVIDIA GPU with at least 6 GB VRAM and an up-to-date driver, and ComfyUI 0.45.0 or later.**

Free disk space: about 6 GB for ComfyUI and 16 GB for all three workflows’ models. You can use just one workflow.

### Automatic

1. Install [Comfy Desktop](https://www.comfy.org/download) or [ComfyUI Portable](https://github.com/Comfy-Org/ComfyUI/releases).
2. At the top of this repository, click the green **Code** button and choose **Download ZIP**. Unzip it to any folder. You can delete this folder after a successful installation (download the archive again for Check.bat and Uninstall.bat).
3. Open the intended ComfyUI and run **Install.bat**. The installer will ask you a few questions and handle the rest.

   If Windows shows “Windows protected your PC”, select **More info → Run anyway**.

4. Find your workflows in the **Workflows** panel on the left. Press W while ComfyUI is open to show it.

**To uninstall**, open the intended ComfyUI and run **Uninstall.bat**.

### Manual

Follow [MANUAL_INSTALL.md](MANUAL_INSTALL.md#english). The steps are also in the Russian **START** note inside each workflow.

## Troubleshooting

Open the intended ComfyUI, run **Check.bat** and follow the instructions. If the issue persists, find `diagnostic_report.txt` next to Install.bat or at the path shown by Check, then send it to the developer on [Telegram](https://t.me/sofiakholina).

## Known issues

- If Windows reports a missing VCRUNTIME140.dll or MSVCP140.dll, install the Microsoft Visual C++ Redistributable: https://aka.ms/vc14/vc_redist.x64.exe
- The older ComfyUI interface shows internal Save 3D settings. Leave them at their defaults.

## License

GPL-3.0 (see LICENSE). Third-party workflow templates and models have their own licenses, listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). s_tools nodes: [sofiakholina-s_tools](https://github.com/sofiakholina/sofiakholina-s_tools).
