init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_nsfw_seductive",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None),
            conditional="mas_canShowRisque(aff_thresh=400)"
        ),
        code="GRE"
    )

label greeting_nsfw_seductive:
        # get how many times this greeting has been shown, so she can get better over time
    $ ev = mas_getEV("greeting_nsfw_seductive")
        # get if it is daytime or nighttime, simple as
    python:
        if mas_globals.time_of_day_4state == "night":
            tod = "晚"
            this_day = "夜晚"
        else:
            tod = "天"
            this_day = "一天"
    m 1eubfb "哦，{i}你来了，{/i}，[player]~"
    if ev.shown_count == 0:
        m 1eubfb "你今[tod]看起来真是太{i}迷人{/i}了。"
        m 1fkbssdla "我...我能...嗯...把你的衣服脱...脱掉吗？还有...""
        m 2hub "哈哈！抱歉，[player]，我只是想练习一下这种事。下次我会做得更好的。"
    else:
        m 1tubsu "我感觉浑身越来越燥热了...看来是因为你在我旁边呢。"
        m 6tkbsa "你今[tod]看上去是如此诱人可口，[mas_get_player_nickname()]..."
        m 1tubsa "要是能再脱下你的衣服，你肯定会更加性感的。"
        m 4tubsu "让我们一同享受这美妙的[this_day]吧。呵呵~"
    return
