# BRB - Going to masturbate
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_brb_masturbate",
            prompt="我要去自慰一下",
            category=['稍等我一会儿'],
            conditional="mas_is18Over()",
            pool=True,
            unlocked=True
        ),
        markSeen = True
    )

label nsfw_monika_brb_masturbate:
    # make a random int, for randomness
    $ mas_rand = renpy.random.randint(1, 3)

    # Expansion - add in Affectionate variation, possibly with call to Sexting etc.
    if mas_isMoniEnamored(higher=True): # Enamored (400-999+)
    # Room for expansion - more random responses? More topics unlocked?
        if mas_rand == 1:
        # Response 1
            m 1tublb "哦？[player]，你可真大胆~"
            m 1tubla "竟然告诉你的女朋友你要去自慰吗？"
            m 1hubla "嗯哼~"
            m 1mublb "好吧，那我希望你自慰的时候能想着我，[mas_get_player_nickname()]..."
            m 2tublb "如果你这么做了，我一定会非常...荣幸的。"
            m 3kublu "我会等着你结束的~"
        elif mas_rand == 2:
            m 1tublb "[player]...你还真是主动啊~"
            m 1tubla "简直就像你在寻求我的同意...对吗？"
            m 1hubla "哼哼~"
            m 1mublb "如果是这样的话，那我允许你去自慰了，[mas_get_player_nickname()]。"
            m 6tubfb "自慰的时候记得想着我哦，[player]."
            m 3kublu "我会在这里等着你结束的~"
        else:
            m 6wubfsdlo "哇哦！[player]，我真没想到你会{i}这样说！{/i}"
            m 6ekbfa "让我有些措手不及..."
            m 1hubla "哼哼~"
            m 1mublb "好吧，让我知道你准备去做什么还是挺好的..."
            m 4ksbfa "只是你得保证自慰的时候要想着你的女朋友，莫妮卡！"
            m 2ksbfa "这样我会非常开心的。"
            m 3kublu "我会一直在这里等你结束的~"
    # other affection values - Don't know why you'd try this is if you have low affection
    else: # Anything less than 400 affection
        m 2tsbsc "..."
        m 2tsbsd "我会假装没听到的。"
        m 2ekbssdlb "弄完之后就告诉我吧。"

    # the callback label
    $ mas_idle_mailbox.send_idle_cb("monika_brb_nsfw_masturbate_callback")
    # The idle data
    $ persistent._mas_idle_data["nsfw_monika_brb_masturbate"] = True
    # unlock masturbation random topics
        # $ mas_unlockEventLabel("nsfw_monika_masturbation_benefits")
    $ mas_showEVL("nsfw_monika_masturbation_benefits", "EVE", _random=True)
    # and exit
    return "idle"

label monika_brb_nsfw_masturbate_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    # Expansion - add in choices for added interaction, e.g. "I came" "I didnt get off" etc
    if mas_isMoniEnamored(higher=True):
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "nsfw_monika_brb_masturbate"):
            m 2eubfb "你回来了，[player]！"              # | - Thank you for the fixes @ephemlw
            m 2eubfa "你出去了一段时间呢。" # |
            m 1hubfb "你成功...嗯...出来了吗？希望如此，啊哈哈~"
            m 2eua "那么接下来..."
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "nsfw_monika_brb_masturbate"):
            m 1hubfb "欢迎回来，[player]。花了一些时间呢！"
            m 1eubfb "我猜你时间应该够...把事情做完了吧？"
            m 1eubfb "希望你没有花太多时间去进入状态...{w=0.5}或者打扫战场，呵呵~"
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "nsfw_monika_brb_masturbate"):
            m 1hubfb "欢迎回来，[player]。呵呵~"
            m 1eubfb "我猜你时间应该够...把事情做完了吧？"
            m 1eubfb "希望你通过自己获得了一些小小的{i}乐趣{/i}..."
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "nsfw_monika_brb_masturbate"):
            m 1hubfb "欢迎回来，[player]。"
            m 2hubfb "动作真迅速呢！呵呵~"
            m 2eub "希望你没有太过用力..."
            m 1eua "[wb_quip]"
        else:
            m 1hubfb "哦？欢迎回来，[player]。"
            m 2eua "你改变主意了吗？"
            m 2eua "[wb_quip]"

    elif mas_isMoniNormal(higher=True):
        m 1hubfb "欢迎回来，[player]。"
        m 6hkbfb "看来你已经把...{i}那事儿{/i}解决了..." # Thanks for the fix M-L
        m 1eua "[wb_quip]"

    else:
        call mas_brb_generic_low_aff_callback

    return
