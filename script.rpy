# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define w = Character('Среда', color="#f15635")
define m = Character('Отче', color="#f7f21a")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene entuz
    play music "audio/menu_theme.mp3"

    show mirror

    w "Лицо в облаке - ни следа в толпе."

    w "Кажется что-то такое было в одной книге..."


    stop music
    scene church
    play music "audio/church_sounds.mp3"
    m "Он утешает нас во всех наших бедах,\n чтобы мы могли утешить других.\n Когда они будут в беде, мы сможем дать им то же утешение,\n которое бог дал нам "
    show father
    m "Что тебя тревожит, сын мой?"

    return
