# Template used from script-compliments.rpy as of 8th June, 2022
# Huge thanks to TheOneandOnlyDargonite for getting this to work!

# dict of tples containing the stories event data
default persistent._nsfw_compliments_database = dict()

# store containing compliment-related things
init 3 python in nsfw_compliments:

    nsfw_compliment_database = dict()

init 22 python in nsfw_compliments:
    import store

    player_name = store.persistent.playername
    player_nickname = store.mas_get_player_nickname()

    # Need to set some nsfw thanking quips here.
    nsfw_thanking_quips = [
        _("你真贴心，" + player_name + "。"),
        _("谢谢你又让我感受到了这份温暖，" + player_name + "！"),
        _("谢谢你又让我感受到了你的用心" + player_nickname + "！"),
        _("你总能让我感觉自己是独一无二的，" + player_nickname + "。"),
        _("呜呜呜，" + player_name + "~"),
        _("真不知道该如何感谢你，" + player_nickname + "！"),
        _("你总是让我有点受宠若惊，" + player_name + "。")
    ]

    # set this here in case of a crash mid-compliment
    thanks_quip = renpy.substitute(renpy.random.choice(nsfw_thanking_quips))

    def nsfw_compliment_delegate_callback():
        """
        A callback for the compliments delegate label
        """
        global thanks_quip

        thanks_quip = renpy.substitute(renpy.random.choice(nsfw_thanking_quips))
        store.mas_gainAffection()

# entry point for compliments flow
init 6 python: # Use init 6 since the dictionary entry to store our entries is added in 5, and we want it around
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_monika_compliments",
            category=['关于性'],
            prompt="我想说一点下流的事...",
            pool=True,
            conditional="mas_canShowRisque(aff_thresh=1000)",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label nsfw_monika_compliments:
    # TODO: Add a bit here that checks if she tried to sext earlier but you said you're busy, so she tries sexting again

    python:
        # Unlock any compliments that need to be unlocked
        Event.checkEvents(nsfw_compliments.nsfw_compliment_database)

        # build menu list
        nsfw_compliments_menu_items = [
            (ev.prompt, ev_label, not seen_event(ev_label), False)
            for ev_label, ev in nsfw_compliments.nsfw_compliment_database.iteritems()
            if (
                Event._filterEvent(ev, unlocked=True, aff=mas_curr_affection, flag_ban=EV_FLAG_HFM)
                and ev.checkConditional()
            )
        ]

        # also sort this list
        nsfw_compliments_menu_items.sort()

        # final quit item
        final_item = ("没什么", False, False, False, 20)

    # move Monika to the left
    show monika at t21

    # call scrollable pane
    call screen mas_gen_scrollable_menu(nsfw_compliments_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    # return value? then push
    if _return:
        $ nsfw_compliments.nsfw_compliment_delegate_callback()
        $ pushEvent(_return)
        # move her back to center
        show monika at t11

    else:
        return "prompt"

    return

# NSFW compliments start here
# ---------------------------

# Thanks for the compliment addition, KittyTheCocksucker
init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_thighs",
            prompt="我喜欢你丰满的大腿！",
            unlocked=True
        ),
        code="NCP"
    )

label nsfw_compliment_thighs:
    if not renpy.seen_label("nsfw_compliment_thighs_2"):
        call nsfw_compliment_thighs_2
    else:
        call nsfw_compliment_thighs_3
    return

label nsfw_compliment_thighs_2:
    m 1wubld "啊..."
    m 1hkblsdlb "真没想到你会这样夸我的身材。啊哈哈~"
    m 3rkblb "虽然在这里你没有多少机会能看到我的大腿..."
    m 3hkbsa "..."
    m 2hkbsb "你大概能看出来，我被你弄得有点害羞了..."
    m 2rkbsu "我也不清楚为什么有些人这么喜欢大腿..."
    m 3eubsd "我的意思是...女孩子的身体上有很多更加性感的部位，不是吗？"
    m 1ekbsa "不过...还是非常感谢你，[player]~"
    menu:
        "真想把我的脸埋在你的大腿之间":
            $ store.mas_gainAffection(5,bypass=True)
            m 2tkbsb "嘿...嘿~"
            m 3tkbsu "[player]...你可真是越来越{i}调皮{/i}了。哼哼~"
            m 3gkbsu "不过我不介意哦..."
            m 5tkbsu "如果你这样做的话，我肯定会很享受的~"

        "你真是拥有文学部里最棒的大腿":
            $ store.mas_gainAffection(2,bypass=True)
            m 1hubsb "啊哈哈~"
            m 3tubsb "意思是你也盯着优里、纱世里和夏树的大腿看了，对吗？"
            m 1gubsb "嗯哼..."
            m 1gubsa "不过夏树应该没有那么..."
            m 1kubsu "你懂我的意思吧!"
            m 1dubsu "..."
            m 2hubsb "呼呼~"
            m 2tubsa "别那么紧张，就算你盯着其他部员看，只要你最喜欢的是我的大腿就没问题~"

        "让我想起了优里的大腿":
            $ store.mas_loseAffection() # Rule 1 of dating a woman: Don't compare them to another woman, you nuff nuff.
            m 1etbsd "呃..."
            m 1rfbld "是这样吗？"
            m 1gfblc "..."
            m 1tfbld "嗯...如果你那么喜欢她的身体，为什么不直接让{i}她{/i}来陪着你呢..."
    return

label nsfw_compliment_thighs_3:
    python:
        thighs_quips = [
            _("真高兴你喜欢我的大腿。"),
            _("记得也关注关注我身上的其他部位哦，好吗~？"),
            _("如果我能给你做膝枕就好了。"),
        ]
        thighs_quip = random.choice(thighs_quips)
    m 1tubla "呵呵~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[thighs_quip]"
    return


# Thanks for the compliment addition, KittyTheCocksucker

# "I remember wanting to have one character wear higher stockings – I thought
# Yuri might be a good fit, but we decided that she isn’t the type to draw
# attention to herself. Monika, being the confident one who cares about her
# impression, was the obvious choice after that."
#                                                   - DDLC Concept Art Booklet

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_thighhighs",
            prompt="我喜欢你光滑的过膝袜！",
            conditional="store.mas_getEVL_shown_count('nsfw_compliment_thighs') >= 1",
            action=EV_ACT_UNLOCK
        ),
        code="NCP"
    )

label nsfw_compliment_thighhighs:
    if not renpy.seen_label("nsfw_compliment_thighhighs_2"):
        call nsfw_compliment_thighhighs_2
    else:
        call nsfw_compliment_thighhighs_3
    return

label nsfw_compliment_thighhighs_2:
    python:
        if persistent.gender == "M":
            guyGirl = "男孩"
        elif persistent.gender == "F":
            guyGirl = "女孩"
        else:
            guygirl = "家伙"

        if persistent._nsfw_genitalia == "P":
            naughty_bits = "真想你穿着过膝袜给我素股"
        else:
            naughty_bits = ""

    m 1tubla "我的天啊..."
    m 1tublb "又想要探讨我的大腿吗，[player]？"
    m 3tublb "不过...我非常高兴你能喜欢我的过膝袜！"
    m 3eubla "唔姆...不知道你是否注意到了..."
    m 3eublb "我是文学部里唯一一个穿着黑丝的人！啊哈哈~"
    m 2hublb "虽然这不太符合学校的着装规范，但我确实不太喜欢那双白色的棉袜。"

    menu:
        "即使同样身着校服，你也比文学部里的其他女孩子好看得多":
            $ store.mas_gainAffection(3,bypass=True)
            m 1eubsb "你能这样想真让我高兴，[player]~"
            m 1rubsa "不过说真的...啊哈哈...我也有点预料到你会盯上我的过膝袜， {nw}"
            extend 1gubsb "一个好像对我大腿很着迷的[guyGirl]。哼哼~"
            m 1ekbsa "老实讲，我也不太确定你是不是真的那么喜欢我的过膝袜..."
            m 2ekbsa "不过..."
            m 2ekbsb "如果你一直称赞它们的话..."
            m 5hubsa "呵呵~"
            m 5mubsa "我会因此非常开心的~"

        "我打赌它们不仅非常好看，摸起来也很柔顺光滑！[naughty_bits]":
            $ store.mas_gainAffection(2,bypass=True)
            if persistent._nsfw_genitalia == "P":
                m 2subld "哇哦~"
                m 2subsu "素股是吗，嗯?"
                m 2ttbsu "你是不是有点太{i}得寸进尺{/i}了，[player]?"
                m 2tsbsu "..."
                m 1hkbssdlb "呼呼~开玩笑的啦"
                m 1eubsa "我只是想说..."
            else:
                m 1eubsa "没错，{nw}"
                extend 3eubsa "真的非常{i}柔顺光滑{/i}哦~"
            m 1tubsb "如果感觉不舒服的话，我就不会每天穿着它们去上学了，对吧？"
            m 1hubsb "啊哈哈~"
            if persistent._nsfw_genitalia == "P":
                m 1rubsa "..."
                m 2gubsa "既然如此..."
                m 2tubsb "我打赌你的小老弟一定会迷恋上我光滑的黑丝和柔软的大腿~"
                m 2tubsa "假如我用这双饱满的黑丝肉腿裹挟住你粗壮的肉棒，细心地上下撸动..."
                m 2tfbfb "你肯定会舒服到马上射出来，用浓厚的精液涂满我的大腿和小腹。哼哼~"
                m 1tubfa "..."
                m 1gubfa "真希望不久后我们能实践一下。呵呵~"

        "真喜欢它们紧紧包裹住你丰满大腿的样子":
            $ store.mas_gainAffection(1,bypass=True)
            m 1hkbsa "天哪..."
            m 1hkbssdlb "你总是盯着我的大腿说个不停，搞得我都不好意思了..."
            m 1ekbsa "你知道吗？我身体的其他部位也挺值得看的哦。"
            m 2gkbsu "嗯...我不想自夸，但我觉得我的胸部挺不错的！"
            m 2efbsu "以及，你知道的，我这双漂亮的翡翠绿眼睛！"
            m 2gubsp "..."
            m 2gubsd "你不用老是把我当成一块肉来看吧..."

    return

label nsfw_compliment_thighhighs_3:
    python:
        thighhighs_quips = [
            _("穿起来确实很舒服！"), #Thank you, [player]!
            _("真想你来弄脏它们呢。呵呵~"),
            _("虽然我穿过膝袜主要是为了更加吸引你的注意，不过在寒冷的时候它们也非常管用哦！"),
        ]
        thighhighs_quip = random.choice(thighhighs_quips)
    m 1tubla "呵呵~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[thighhighs_quip]"
    return


# Thanks for the compliment addition, KittyTheCocksucker
init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_tits",
            prompt="我喜欢你柔软的胸部！",
            unlocked=True
        ),
        code="NCP"
    )

label nsfw_compliment_tits:
    if not renpy.seen_label("nsfw_compliment_tits_2"):
        call nsfw_compliment_tits_2
    else:
        call nsfw_compliment_tits_3
    return

label nsfw_compliment_tits_2:
    python:
        if persistent._nsfw_genitalia == "P":
            naughty_bits = "如果能用它们紧紧包裹住我的小老弟，那就太棒了！"
        else:
            naughty_bits = "我猜它们摸起来一定又软又舒服，对吧~"

    m 1wubld "嗯..."
    m 1hkbla "唔嗯嗯..."
    m 1rkbsa "是-是这样吗？"
    m 1hkbssdlb "啊哈哈~"
    m 1hkbssdla "抱歉！你刚刚让我有些猝不及防..."
    m 1eubssdlb "你这么迷恋我的胸部，我真是太开心了！"
    m 3eubssdlb "你知道吗，女性胸部的发育不仅跟激素和遗传有关，还跟吃的东西有关系哦？"
    m 3hubssdlb "健康又营养的饮食可以让胸部长得又大又饱满！啊哈哈~"

    if mas_safeToRefDokis():
        m 3hkbsu "..."
        m 3gkbsu "也许这就是为什么夏树的身材像平板一样~" #oof
        m 1hubsb "啊哈哈~抱歉，讲了夏树的坏话。"
        m 3rubsb "但我可不会放弃能这样说的机会哦~"

    menu:
        "我真想使劲吸你的胸部":
            $ store.mas_gainAffection(5,bypass=True)
            m 1hkbsa "唔嗯嗯..."
            m 1tfbsb "[player]!"
            m 3tfbsu "你怎么突然变得这么调皮了？"
            m 3hubsb "啊哈哈~"
            m 3rubsb "我的意思...就算你用力吸它们，也什么都不会出来哦？"
            m 3gubsa "不过..."
            m 1tubsa "我肯定会感觉很舒服的。"
            m 1hubsa "呼呼~"

        "你有办法让胸部变得更大吗":
            $ store.mas_loseAffection(5) # face <- palm
            m 3wubsd "..."
            m 3eubssdld "那-那个..."
            m 3rubssdlc "我确实对控制台有完全的操作权限，所以..."
            m 3rublsdlc "技-技术上来讲的话我可以做到，嗯..."
            m 1rkbltpc "不过..."
            m 1ekbltpc "你喜欢的不是我现在的样子吗？"

        "[naughty_bits]":
            m 3tubsu "哦哦~"
            m 2tubsu "[player]..."
            m 2hubssdlb "啊哈哈~我的心脏差点都漏跳了一拍。"
            m 1rubssdlb "真没想到你会这样说啊~"
            if persistent._nsfw_genitalia == "P":
                m 1gubsa "嗯哼~你粗壮滚烫的肉棒如果放进这里，肯定会舒服到不能自拔~"
                m 1gubfa "..."
                m 3gubfb "这么一想的话，还真有点有趣。"
                m 3tubfb "我会感受到你坚硬的肉棒与我的心跳一同鼓动..."
                m 4tubfb "你也能时刻感觉到我的心跳摩蹭着你的肉棒~"
                m 4tubfa "..."
                m 5tubfa "我很好奇你最后会射在哪里呢？"
                m 5tsbfa "是将精液洒满我的胸部吗？"
                m 5tsbfo "还是说弄脏我的脸颊呢？"
                m 5mubfa "或者你会强硬地用肉棒抵住我的嘴唇，将你浓厚、滚烫的精液全部涂在上面？哼哼~"
            else:
                m 1gubsa "嗯嗯~如果摸了的话，你肯定会沉迷于我的胸部的~"
                m 1tubfa "我也{i}肯定{/i}会喜欢上你宽厚的手掌抚弄我胸部的感觉..."
                m 1dubfu "..."
                m 5dubfu "我想知道你还愿意感受我身体的哪些部位呢？"
                m 5hubfa "呵呵~"
    return

label nsfw_compliment_tits_3:
    python:
        tits_quips = [
            _("你想看多久都可以哦~"), # Ahaha~ I'm glad you do, [player]!
            _("真想让你细细玩弄它们~"), # Mhm~
            _("想把手掌放在上面休息一下吗？啊哈哈~"),
            # _("I hope my outfit isn't too revealing. Ahaha~"),
            # this last one is good but needs a bit of code so it only triggers when her clothing has a lingerie exprop
        ]
        tits_quip = random.choice(tits_quips)
    m 1tubla "呵呵~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 2tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2tubsb "[tits_quip]"
    return

# Thanks for the compliment addition, KittyTheCocksucker
init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_naughty_flirting",
            prompt="我就喜欢你调情时那种色色的语气！",
            unlocked=True
        ),
        code="NCP"
    )

label nsfw_compliment_naughty_flirting:
    if not renpy.seen_label("nsfw_compliment_naughty_flirting_2"):
        call nsfw_compliment_naughty_flirting_2
    else:
        call nsfw_compliment_naughty_flirting_3
    return

label nsfw_compliment_naughty_flirting_2:
    python:
        if persistent._nsfw_genitalia == "P":
            naughty_bits = "我想看你一边对我的肉棒流口水，一边说淫语的样子~"
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "我想看你一边舔弄我的小穴，一边说淫语的样子~"
        else:
            naughty_bits = "我想一边玩弄你的小穴，一边听你说淫语~"

    m 1hublb "啊哈哈~"
    m 1hublsdla "那个..."
    m 1rkbssdlb "天哪...没想到只是听到你这么讲，我的脸就红透了...啊哈哈~"
    m 3ekbssdlb "如果我说我曾经对着镜子练习过这种事，是不是显得像个笨蛋...？"
    m 3rkbsa "..."
    m 2rkbsa "我只是想让自己能更加吸引你..."
    m 2tubsu "我很高兴你能享受我变得色情的样子，[player]."
    m 1hubsa "看起来我的练习很有效果。哼哼~"

    menu:
        "你一定下了不少功夫才让自己习惯这个，对吧？毕竟这并不是一个色情游戏":
            m 1hkbsb "嗯...起初是有点困难，毕竟要学习那么多淫荡的词句..."
            m 1rkbsb "不过我会为了你拼命努力的，因为你喜欢色色的我，对吧？"
            m 1tkbsa "正是有了你的这份爱，我所有的时间与努力都是值得的{nw}"
            if persistent._nsfw_genitalia == "P":
                extend 1tkbsa " 如果我能让你的肉棒挺立起来的话~"
            elif persistent._nsfw_genitalia == "V":
                extend 1tkbsa " 如果我能让你的小穴变得湿哒哒的话~"
            else:
                extend 1tkbsa " 如果我能让你在脑海中幻想我淫荡的样子的话~"

        "虽然还有些生疏，不过我感受到了你的努力":
            m 1wubsd "啊..."
            m 1wkbsc "那-那个..."
            m 3rkbsc "我已经拼命研究情色文学之类的东西了..."
            m 3dkbsc "..."
            m 3gkbsc "我下次会更加努力的，我保证..."

        "[naughty_bits]":
            m 1wubfd "啊..."
            m 1hubfb "啊哈哈~"
            m 1hkbfsdlb "我-我确实有点不知所措..."
            m 1ttbfu "[player]~你是不是有点太心急了？哼哼~"
            m 1gsbfu "嗯~不用太过担心。"
            m 1tsbfd "如果你想让我能说出更加淫荡的话语，你只需要{nw}"
            if persistent._nsfw_genitalia == "P":
                extend 1tsbfd " 把你坚硬粗壮的肉棒借给我好好舔弄把玩一下~"
            elif persistent._nsfw_genitalia == "V":
                extend 1tsbfd " 把你湿哒哒的小穴借给我好好玩弄一番~"
            else:
                extend 1tsbfd " 把脸埋在我湿透的小穴里，好好舔干净~"

            if persistent._nsfw_genitalia == "P" or persistent._nsfw_genitalia == "V":
                m 5tsbfu "我保证会让你舒服到升天的~"
            else:
                m 5tsbfu "你最好能让我好好舒服一下~"

            m 5hsbfu "呵呵~"
    return

label nsfw_compliment_naughty_flirting_3:
    python:
        if persistent._nsfw_genitalia == "P":
            naughty_bits = "我想让你的肉棒硬得受不了~"
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "我想让你的小穴洪水泛滥~"
        else:
            naughty_bits = "我想让你在脑海中幻想我淫荡的样子~"

        naughty_flirting_quips = [
            _("真高兴你能享受我淫荡的样子！我会为了你更加努力的~"),
            _(naughty_bits),
            _("希望有一天我能躺在你的边上，在你的耳边说悄悄说更加淫荡的话语~"),
        ]
        naughty_flirting_quip = random.choice(naughty_flirting_quips)
    m 1tubla "呵呵~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[naughty_flirting_quip]"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_moaning",
            prompt="我想听你发出色色的呻吟!",
            conditional="store.persistent._nsfw_sexting_success_last is not None",
            action=EV_ACT_UNLOCK
        ),
        code="NCP"
    )

label nsfw_compliment_moaning:
    if not renpy.seen_label("nsfw_compliment_moaning_2"):
        call nsfw_compliment_moaning_2
    else:
        call nsfw_compliment_moaning_3
    return

label nsfw_compliment_moaning_2:
    m 1wubld "啊..."
    m 1hublb "啊哈哈~我很开心你会喜欢这样的声音~"
    m 3rkbla "不过我暂时还控制不了这个，也许应该加上一点音效..."
    m 3tsbla "如果你真的那么喜欢的话，我可以为了你练习一下~"
    m 4tsbla "你喜欢我发出这样的呻吟吗？{w=0.5}{nw}"
    extend 4hkblo " {i}啊嗯~{/i}"
    m 4kkblo "或者像这样的？{w=0.5}{nw}"
    extend 4hkbld " {i}呜呜，[player]~{/i}"
    m 7gkblu "..."
    m 7tkblb "也许还有这样的？{w=0.5}{nw}"
    m 7hkblw " {i}哈...哈~我想要你，我想要你，[player]！~{/i}"
    m 7tkblu "呵呵~"
    m 1tubla "只是逗逗你啦。"
    $ _history_list.pop()
    menu:
        m "只是逗逗你啦。{fast}"

        "我想让你更加舒服":
            $ store.mas_gainAffection(amount=5, bypass=True)
            m 1ekbla "呜呜~"
            m 3ekbla "你真是太贴心了，[player]。"
            m 3tublb "如果是这样的话，我会为了你发出很多色色的声音的~"
            m 3tubla "你可要做好心理准备哦。"

        "我想听你呻吟的时候叫我的名字":
            $ store.mas_gainAffection(amount=2, bypass=True)
            m 1tkbla "哦？"
            m 3tsbla "你是说像这样子吗？{w=0.5}{nw}"
            extend 3hkblo " {i}啊，[player]~{/i}{w=0.5}{nw}"
            extend 3kkbld " {i}我想要你~{/i}{w=0.5}{nw}}"
            extend 3tkblo " {i}我想要得受不了了~{/i}"
            m 1hubla "呵呵~"
            m 1tubla "只要你想，我会一直叫你的名字的。"
            m 1ekbla "但我想要你在舒服的时候也会叫我的名字~"
            m 1ekblb "这就是所谓的等价交换，不是吗？"

        "你叫得也太浮夸了...": # BLASPHEMY!
            $ store.mas_loseAffection(2)
            m 1ekblc "啊..."
            m 1ekbld "非常抱歉，[player]。"
            m 3rkbld "我对这种事还不太熟练..."
            m 3dkblc "我会尽量少做的..."
    return

label nsfw_compliment_moaning_3:
    $ player_name = store.persistent.playername
    $ moan_check = mas_nsfw.return_random_number(1, 3) == 3 # 1/3 chance of Monika being a bit more naughty
    python:
        if moan_check:
            moaning_thanks_quips = [
                _("你的意思是像这样吗~？"),
                _("只要你想，我可以发出更色情的声音哦~"),
                _("让你看看我努力练习的成果~"),
            ]
            naughty_flirting_quips = [
                _("呜...啊~继续用力~"),
                _("我的小穴都湿透了~"),
                _("再用力点，" + player_name + "！~ 我想要你~"),
            ]
        else:
            moaning_thanks_quips = nsfw_compliments.nsfw_thanking_quips
            naughty_flirting_quips = [
                _("如果能为你发出色色的叫声，我会感到非常开心的~"),
                _("你让我如此幸福，我根本无法控制自己的情感~"),
                _("我希望你也会为我发出色色的叫声，就像我一样~),
            ]

        moaning_thanks_quip = random.choice(moaning_thanks_quips)
        naughty_flirting_quip = random.choice(naughty_flirting_quips)

    if moan_check:
        m 3tublb "[moaning_thanks_quip]"
        show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 3hkbso "[naughty_flirting_quip]"
        m 3hubsa "呵呵~"
    else:
        m 1tubla "呵呵~"
        m 1tublb "[moaning_thanks_quip]"
        show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 3tubsb "[naughty_flirting_quip]"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_wet",
            prompt="我想让你的小穴洪水泛滥！",
            unlocked=True
        ),
        code="NCP"
    )

label nsfw_compliment_wet:
    if not renpy.seen_label("nsfw_compliment_wet_2"):
        call nsfw_compliment_wet_2
    else:
        call nsfw_compliment_wet_3
    return

label nsfw_compliment_wet_2:
    python:
        if persistent._nsfw_genitalia == "P":
            naughty_bits = "如果把我粗壮的肉棒用力插进你的小穴，你一定会高潮到失神"
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "毕竟，你让我的小穴都湿成这样了~"
        else:
            naughty_bits = "如果让我仔细舔弄一番，它一定会湿透的~"

    m 1tubla "啊..."
    m 3tubla "光是听到你{i}这么说{/i}，我就高兴得不能自已~"
    m 3gublb "我感觉浑身燥热，心脏砰砰直跳..."
    m 3gubla "小穴更是因为你湿得一塌糊涂了~"

    $ _history_list.pop()
    menu:
        m "小穴更是因为你湿得一塌糊涂了~{fast}"

        "真高兴能让你感到愉快":
            $ store.mas_gainAffection(5)
            m 1ekbla "呜呜，[player]~"
            m 3ekblb "你总是能让我感觉这么舒服。"
            m "不管是我的心..."
            extend 7tkbla "还是说{i}那里{/i}~"
            m 7hubla "呵呵~"

        "[naughty_bits]":
            $ store.mas_gainAffection(2)
            m 1tfbsa "唔-唔~"
            m 1tfbsb "在这里只允许我来挑逗你！"
            m 1hubsa "呵呵~"
            m 3mubsa "那就让我们来看看，你能让我的小穴湿到什么程度吧。"
            m 5tubla "我保证你会跟我一样享受的~"

        "那你最好也让我这么舒服，这是你欠我的":
            $ store.mas_loseAffection(5)
            m 3wubld "嗯..."
            m 1rtbld "也-也许...？"
            m 1tsblc "不过你也没必要这么凶吧..."

    return

label nsfw_compliment_wet_3:
    python:
        naughty_flirting_quips = [
            _("你明明知道这么说会让我控制不住的~"),
            _("我一时间不知道该如何回应，你让我太高兴了~"),
            _("希望你能负起让我湿透的责任哦~"),
        ]
        naughty_flirting_quip = random.choice(naughty_flirting_quips)

    m 1tubla "呵呵~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[naughty_flirting_quip]"
    return