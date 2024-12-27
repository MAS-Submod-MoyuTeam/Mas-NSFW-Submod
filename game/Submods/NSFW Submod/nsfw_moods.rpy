init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            "nsfw_mood_horny",
            prompt="...想要色色.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True,
            ),
        code="MOO"
    )

label nsfw_mood_horny:
    # Check when player's last succesful sexting session was
    if store.persistent._nsfw_sexting_success_last is not None:
        $ timedelta_of_last_success = datetime.datetime.now() - store.persistent._nsfw_sexting_success_last
        $ time_since_last_success = datetime.datetime.now() - timedelta_of_last_success
    else:
        $ time_since_last_success = datetime.datetime.today() - datetime.timedelta(days=1)

    # If the player's last succesful sexting session was less than three hours ago
    if (time_since_last_success >= datetime.datetime.today() - datetime.timedelta(hours=3) or not mas_canShowRisque(aff_thresh=1000)) and store.persistent._nsfw_sexting_success_last is not None:
        m 2wubld "哇哦！"
        m 2rkblc "抱歉，[player]。心里躁动不安的话很影响注意力吧。"
        m 3rkblb "如果积攒得太多的话，或许你需要花几分钟来..."
        m 3dkblu "嗯嗯嗯..."
        m 3ekblb "释~放一下..."
        m 1hubla "释放的时候一定要想着我哦！"
        if mas_canShowRisque(aff_thresh=1000):
            m 1hubsa "..."
            m 1gubsa "如果我能到你身边的话，或者我可以{i}伸出援手{/i}。"
            m 1hubsa "呵呵~"
        return

    m 1tua "哦？原来是这样吗，[player]？"
    m 3tub "那么...我知道一个好方法可以让你{i}放松{/i}下来..."
    m 3tta "我来给你搭把手吧？"

    $ _history_list.pop()
    menu:
        m "我来给你搭把手吧？{fast}"

        "好的":
            $ store.persistent._nsfw_sext_hot_start = True # Might change this in the future if we make Monika's horny level change depending on other events. Making this an IF statement rather than forcing her to be horny.
            m 4tublb "哼哼，那么现在听从我的指示。"
            m 5tublb "把你积攒已久的欲望全部对着我发泄出来，好好享受吧[mas_get_player_nickname()]~"

            call nsfw_sexting_init

        "不用":
            m 3eka "没关系，[player]。"
            m 1hua "如果你需要我的帮助，我会一直在这里等着你~"
    return