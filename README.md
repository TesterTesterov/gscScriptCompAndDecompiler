# gscScriptCompAndDecompiler
Tool for decompiling, compiling and rebuilding scripts .gsc from the visual novel's engine codeX RScript (also known as Liar-soft Engine or raiL-soft Engine).

Средство для декомпляции, компиляции и перестройки скриптов .gsc движка визуальных новелл codeX RScript, известного также как Liar-soft Engine или raiL-soft Engine.

The tool supports two GUI languages: English and Russian.

Средство поддерживает два языка графического интерфейса: русский и английский.

There was some tools for the formats ealier, but it was always simple string dumpers. Sometime with an additional functionality.

Ранее для сего формата были прочие средства, но все они были простыми дамперами строк. Иногда с дополнительным функционалом.

Tested on:
- [Kusarihime \~Euthanasia\~](https://vndb.org/v37) <for the most part>
- [Sekien no Inganock -What a Beautiful People-](https://vndb.org/v417) <for the most part>
- [Hiragumo-chan -Sengoku Gekokujou Monogatari-](https://vndb.org/v10182) <for the some part>

Протестировано на:
- [Принцесса порчи: Эвтаназия](https://vndb.org/v37) <по большей части>
- [Инганок ярчайшего пламени: Как прекрасны люди](https://vndb.org/v417) <по большей части>
- [Хирагумо-тян: Моногатари о "Высший побеждает высшего" эпохи Сэнгоку](https://vndb.org/v10182) <в некоторой степени>

Uncomplete game's on the engine list you can see on [here](https://vndb.org/r?fil=engine-codeX_01RScript).

Неполный список игр на данном движке вы можете просмотреть [здесь](https://vndb.org/r?fil=engine-codeX_01RScript).

For edition of the engine's archieves (.xfl), canvases (.lwg) and images (.wcg) use either [RailTools](https://github.com/EusthEnoptEron/RaiLTools) or [GARbro](https://github.com/morkt/GARbro) (the latter don't suit for canvases editing).

Для изменения архивов (.xfl) движка, холстов (.lwg) и картинок (.wcg) используйте или [RailTools](https://github.com/EusthEnoptEron/RaiLTools), или [GARbro](https://github.com/morkt/GARbro) (последнее средство не подходит для редактирования холстов).

# Common / Общее

This program was developed for correctly working with .gsc files of the engine codeX Rscript, which also called as Liar-soft Engine and raiL-soft Engine. The engine is rather simple much like it's formats, for example .gsc, with which through may be some problematic moments. Still the moments are ceasing by the specific decompile and compile. But the scheme can also cause problems it some situations.

This program allow you to:
1. Rebuild .gsc-files from themselves so you can optimize them, for in many of .gsc-files there may be some trash elements. For example some number of zeros in the end. But this command is not garantee that all trash elements will be removed. This command also allow you to see .gsc-file's parametrs and unknown commands. It may be useful for code analysis.\2. .gsc to .txt decomple. It allow you to edit scripts as you like (with limitations of syntax, of course). For example, with this tool you can easily add new message.
3. .txt to .gsc compile. This allow you to rebuild .gsc from decompiled and may be edited ealier code. It doesn't need an ealier .gsc to present for run.

For usage:
1. Drag the .gsc script or .txt with decompiled data to the tool directory.
2. Write the file name in the tool entry and push the "DEFINE".
3. Use the commands below.

Данная программа разработана для корректной работы с файлами .gsc движка codeX RScript, известным также как Liar-soft Engine и raiL-soft Engine. Движок относительно простой, как и относительно просты его форматы, в частности .gsc, с которым, впрочем, есть проблематичные моменты, что купируются своеобразной схемой декомпиляции и компиляции. Из-за которой, впрочем, в некоторых случаях возможны проблемы.

Данная программа позволяет:
1. Перестраивать .gsc-файлы из самих себя, тем самым по сути их оптимизируя, ибо в ряде .gsc-файлов могут содержаться некоторые мусорные элементы, в частности остаточные нули в конце. Тем не менее, не факт, что все мусорные элементы будут прибраны. Также позволяет просматривать параметры .gsc и ход неизвестный команд, что может быть полезно при анализе кода.
2. Декомпиляция .gsc в .txt, позволяющая сколь угодно (в рамках синтаксиса, команд и прочего) редактировать скрипты. Например, с помощью средства добавить новое сообщение проще простого.
3. Компиляция .txt в .gsc. Она в свою очередь позволяет пересобирать .gsc на основе импровизированного разобранного кода. Для данной команды старый .gsc-скрипт не требуется.

Для использования:
1. Перетащите либо скрипт .gsc, либо файл .txt с декомпилированными данными в директорию средства.
2. Напишите его имя в поле ввода и нажмите "ОПРЕДЕЛИТЬ".
3. Используйте комманды снизу.

# Commands / Команды

Unfortunately, the number of known commands aren't big (but not of the structures). It may change it the future. All known commands are defined in decomilated file as a string.

Well, let's show you a basic known commands with the arguments:

- 3 (0x03): JUMP_UNLESS.
Arguments: [label]. (In the original script offset from the beginning of command block).
- 5 (0x05): JUMP.
Arguments: [label]. (In the original script offset from the beginning of command block).
- 12 (0x0C): CALL_SCRIPT.
Arguments: [script number, ???].
- 13 (0x0D): PAUSE.
Arguments: [time in seconds].
- 14 (0x0E): CHOICE:
Arguments: [???, ???, ???, ???, ???, ???, ???, -1, -1, ???, ???, ???, ???, ???, ???].
In the original script is not -1, but choice's strings.
- 20 (0x14): IMAGE_GET.
Arguments: [image index (from the name), ???].
- 26 (0x1A): IMAGE_SET.
Arguments: [].
- 28 (0x1C): BLEND_IMG.
Arguments: [???, type1, type2].
- 30 (0x1E): IMAGE_DEF.
Arguments: [???, ???, ???, ???, ???, ???].
- 81 (0x51): MESSAGE.
Arguments: [???, voice index (from the name), ???, -1, -1, ???].
In a .gsc itself is not a -1, but a string numbers.
- 82 (0x52): APPEND_MESSAGE.
Arguments: [???, ???, ???, ???, -1, ???].
In a .gsc itself is not a -1, but a string numbers.
- 121 (0x79): GET_DIRECTORY.
Arguments: [???, -1].
In a .gsc itself is not a -1, but a string numbers.
- 200 (0xC8): READ_SCENARIO.
Arguments: [label, ???, ???, ???, ???, ???, ???, ???, ???, ???, ???].
- 255 (0xFF): SPRITE.
Arguments: [mode, position, image index, ???, ???].
- 13568 (0x3500): AND.
Arguments: [???, ???, ???].
- 18432 (0x4800): EQUALS.
Arguments: [???, ???, ???].
- 21504 (0x5400): GREATER_EQUALS.
Arguments: [???, ???, ???].
- 43520 (0xAA00): ADD.
Arguments: [???, ???, ???].
- 61696 (0xF100): ASSIGN.
Arguments: [???, ???].

Увы, команд известно мало (но не их структур), а их аргументов ещё меньше. Что, впрочем, может измениться в будущем. Всякая известная команда в файле обозначена некоторой строкой.

Итак, приведём базовые известные команды с аргументами:

- 3 (0x03): JUMP_UNLESS.
Аргументы: [метка]. (В оригинальном скрипте смещение относительно начала секции команд).
- 5 (0x05): JUMP.
Аргументы: [метка]. (В оригинальном скрипте смещение относительно начала секции команд).
- 12 (0x0C): CALL_SCRIPT.
Аргументы: [номер скрипта, ???].
- 13 (0x0D): PAUSE.
Аргументы: [время в секундах].
- 14 (0x0E): CHOICE:
Аргументы: [???, ???, ???, ???, ???, ???, ???, -1, -1, ???, ???, ???, ???, ???, ???].
В оригинальном скрипте вместо -1 строки-выборы, порою начинающиеся с <*>.
- 20 (0x14): IMAGE_GET.
Аргументы: [индекс картинки (из имени), ???].
- 26 (0x1A): IMAGE_SET.
Аргументы: [].
- 28 (0x1C): BLEND_IMG.
Аргументы: [???, тип1, тип2].
- 30 (0x1E): IMAGE_DEF.
Аргументы: [???, ???, ???, ???, ???, ???].
- 81 (0x51): MESSAGE.
Аргументы: [???, индекс гласа (из имени), ???, -1, -1, ???].
В самом .gsc вместо "-1" номера строк!
- 82 (0x52): APPEND_MESSAGE.
Аргументы: [???, ???, ???, ???, -1, ???].
В самом .gsc вместо "-1" номера строк!
- 121 (0x79): GET_DIRECTORY.
Аргументы: [???, -1].
В самом .gsc вместо "-1" номера строк!
- 200 (0xC8): READ_SCENARIO.
Аргументы: [label, ???, ???, ???, ???, ???, ???, ???, ???, ???, ???].
- 255 (0xFF): SPRITE.
Аргументы: [режим, позиция, индекс картинки, ???, ???].
- 13568 (0x3500): AND.
Аргументы: [???, ???, ???].
- 18432 (0x4800): EQUALS.
Аргументы: [???, ???, ???].
- 21504 (0x5400): GREATER_EQUALS.
Аргументы: [???, ???, ???].
- 43520 (0xAA00): ADD.
Аргументы: [???, ???, ???].
- 61696 (0xF100): ASSIGN.
Аргументы: [???, ???].

# Syntax / Синтаксис

For those who desire for scripts to edit it's very important. The syntax is rather simple, but it have some specific moments.

- "$" is the string's beginning is for one-string comment.
- "#" in the string's beginning is for defination of command.
- "[..., ..., ...]" is for function argument's splitted with "," form. It goes strictly on the next line after the command defination.
- "@" is a label, to which some arguments are connecting.
- An "-1" argument means it connected with next string index.
- ">" is for string beginning.
After its goes mark of primar index of string or -1. If it's -1, the string is connected. Connected strings always goes after the defination of connected arguments.

**DO NOTE: INDEXES AFTER ">" SHOWS ONLY PRIMAR INDEXES! THEN COMPILE PROGRAM TAKE A STRING INDEX ONLY FROM THE NUMBER OF ">" IN SCRIPT!
DO NOTE: NOT AN ALL OF CONNECTED INDEXES WAS FOUND!**

Для тех, кто скрипты именно редактировать жаждет, сие крайне важно знать. Синтаксис в целом прост, но имеет ряд особенностей.

- "$" в начале строки обозначает однострочный комментарий.
- "#" в начале строки есть определение команды.
- "[..., ..., ...]" есть форма описания аргументов функции (разделяются запятой) и следует сразу после определения команды.
- "@" есть метка, на кою ссылаются некоторые команды.
- Аргумент "-1" значит, что он связан с индексом следующей строки.
- ">" обозначает строк начало.
После сего идёт либо показатель изначального индекса строки, либо -1. -1 значит, что строка связанная. Связанные строки всегда следуют после задачи связанных аргументов.

**ВАЖНО: ИНДЕКСЫ ПОСЛЕ ">" ОТОБРАЖАЮТ ЛИШЬ ИЗНАЧАЛЬНЫЕ ИНДЕКСЫ! ПРИ КОМПИЛЯЦИИ ИНДЕКС СТРОКИ БЕРЁТСЯ ЛИШЬ ИЗ НОМЕРА ">" В СКРИПТЕ!
ВАЖНО: НЕ ВСЕ СВЯЗАННЫЕ ИНДЕКСЫ БЫЛИ НАЙДЕНЫ!**
