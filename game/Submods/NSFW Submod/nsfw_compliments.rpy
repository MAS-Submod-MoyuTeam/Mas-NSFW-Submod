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
            category=['sex'],
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
            prompt="我喜欢你的大腿！",
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
            prompt="我喜欢你的过膝袜！",
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
                m 2tubsa "I'm sure if I moved my legs, up and down, nicely jerking your massive dick with my thighs..."
                m 2tfbfb "You would ejaculate all over my legs and belly in no time. Ahaha~"
                m 1tubfa "..."
                m 1gubfa "I hope we can try that soon. Ehehe~"

        "I love how they wrap around your thick thighs.":
            $ store.mas_gainAffection(1,bypass=True)
            m 1hkbsa "Gosh..."
            m 1hkbssdlb "You keep making me blush with all this talk about my thighs..."
            m 1ekbsa "The other parts of my body are nice to look at too, you know."
            m 2gkbsu "Like...I don't like to brag, but I think I have pretty nice breasts!"
            m 2efbsu "Plus, you know, my eyes are also up here!"
            m 2gubsp "..."
            m 2gubsd "You don't always need to look at me like I'm just a piece of meat..."

    return

label nsfw_compliment_thighhighs_3:
    python:
        thighhighs_quips = [
            _("They're really comfy too!"), #Thank you, [player]!
            _("I can't wait for you to make a mess over them. Ehehe~"),
            _("I wear them mainly to stand out, but they can also come in handy when it's cold outside!"),
        ]
        thighhighs_quip = random.choice(thighhighs_quips)
    m 1tubla "Ehehe~"
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
            prompt="I love your breasts!",
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
            naughty_bits = "I bet they'd feel nice and soft if I rested my dick between them."
        else:
            naughty_bits = "I bet they'd feel nice and soft if I felt them up~"

    m 1wubld "Uhh..."
    m 1hkbla "Ahem..."
    m 1rkbsa "I-is that so?"
    m 1hkbssdlb "Ahaha~"
    m 1hkbssdla "Sorry! You just caught me off-guard, that's all."
    m 1eubssdlb "I'm really glad you like them!"
    m 3eubssdlb "Did you know that the growth of a woman's breasts are not only affected by hormones and genetics, but by what we eat as well?"
    m 3hubssdlb "Healthy and nutritious meals help our boobs grow nice and round! Ahaha~"

    if mas_safeToRefDokis():
        m 3hkbsu "..."
        m 3gkbsu "I guess that explains why Natsuki was so flat, huh?" #oof
        m 1hubsb "Ahaha~ Sorry, that was a bad joke."
        m 3rubsb "I couldn't let that opportunity slip by~"

    menu:
        "I'd love to suck on your breasts.":
            $ store.mas_gainAffection(5,bypass=True)
            m 1hkbsa "Ahem..."
            m 1tfbsb "[player]!"
            m 3tfbsu "Why did you get so naughty out of nowhere like that?"
            m 3hubsb "Ahaha~"
            m 3rubsb "I mean...I don't know if anything would come out if you did suck on them..."
            m 3gubsa "But..."
            m 1tubsa "I'm sure it would feel really nice if you did that."
            m 1hubsa "Ehehe~"

        "Can you make them bigger?":
            $ store.mas_loseAffection(5) # face <- palm
            m 3wubsd "..."
            m 3eubssdld "I-I mean..."
            m 3rubssdlc "I do have full control over the console, so..."
            m 3rublsdlc "T-technically I could do that, yeah..."
            m 1rkbltpc "But..."
            m 1ekbltpc "Don't you love me the way I am now?"

        "[naughty_bits]":
            m 3tubsu "Ooo~"
            m 2tubsu "[player]..."
            m 2hubssdlb "Ahaha! My heart skipped a beat just now."
            m 1rubssdlb "I didn't expect you to say that~"
            if persistent._nsfw_genitalia == "P":
                m 1gubsa "Mmm~ I'm sure your hard, throbbing cock would feel really nice between my breasts~"
                m 1gubfa "..."
                m 3gubfb "It's kind of funny if you think about it."
                m 3tubfb "I would feel your dick pulsating against my heart..."
                m 4tubfb "And you would feel my heart pulsating against your dick~"
                m 4tubfa "..."
                m 5tubfa "I wonder where you'd unload your cum when you finished?"
                m 5tsbfa "Would it be all over my breasts?"
                m 5tsbfo "Maybe on my face?"
                m 5mubfa "Or would you push forward, between my lips, and release your thick, creamy load there? Ehehe~"
            else:
                m 1gubsa "Mmm~ I'm sure your hands would enjoy the feeling of my breasts~"
                m 1tubfa "And I would {i}really{/i} enjoy the feeling of your hands playing with my breasts..."
                m 1dubfu "..."
                m 5dubfu "I wonder where else on my body you might like to feel me up?"
                m 5hubfa "Ehehe~"
    return

label nsfw_compliment_tits_3:
    python:
        tits_quips = [
            _("You can look at them all you want~"), # Ahaha~ I'm glad you do, [player]!
            _("I can't wait for you to fondle them~"), # Mhm~
            _("Want to rest your head on them? Ahaha~"),
            # _("I hope my outfit isn't too revealing. Ahaha~"),
            # this last one is good but needs a bit of code so it only triggers when her clothing has a lingerie exprop
        ]
        tits_quip = random.choice(tits_quips)
    m 1tubla "Ehehe~"
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
            prompt="I love how naughty you talk when we're flirting!",
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
            naughty_bits = "I'd love to hear you talk naughty while you're slobbering over my cock~"
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "I'd love to hear you talk naughty while you're eating out my pussy~"
        else:
            naughty_bits = "I'd love to hear you talk naughty while I'm eating out your pussy~"

    m 1hublb "Ahaha~"
    m 1hublsdla "Well..."
    m 1rkbssdlb "Gosh... I can't believe I'm getting so red just from you saying that...Ahaha~"
    m 3ekbssdlb "Is it too nerdy to say that I practiced in the mirror...?"
    m 3rkbsa "..."
    m 2rkbsa "I wanted to get better so I can arouse you more..."
    m 2tubsu "I'm glad you enjoy how naughty I can get, [player]."
    m 1hubsa "It means my practice paid off. Ehehe~"

    menu:
        "I bet you had to work hard to tune your brain to it. This wasn't a porn game to begin with, after all.":
            m 1hkbsb "Yeah...it was a little bit difficult at first, having to learn so many lewd phrases and stuff..."
            m 1rkbsb "But since you like when I do it, I must be doing a good job at it, right?"
            m 1tkbsa "And all the time and energy spent on it was totally worth it{nw}"
            if persistent._nsfw_genitalia == "P":
                extend 1tkbsa " if I can make your dick hard~"
            elif persistent._nsfw_genitalia == "V":
                extend 1tkbsa " if I can make your pussy wet~"
            else:
                extend 1tkbsa " if I can give you naughty thoughts about me~"

        "It does need some polishing here and there, but I appreciate the effort.":
            m 1wubsd "Oh..."
            m 1wkbsc "W-well..."
            m 3rkbsc "I already spent a bunch of time studying erotica and stuff..."
            m 3dkbsc "..."
            m 3gkbsc "I'll try to work even harder, I guess..."

        "[naughty_bits]":
            m 1wubfd "Oh..."
            m 1hubfb "Ahaha~"
            m 1hkbfsdlb "T-that certainly caught me off-guard..."
            m 1ttbfu "[player]~ Aren't you getting a little bit ahead of yourself there? Ehehe~"
            m 1gsbfu "Mmm~ Don't worry about it."
            m 1tsbfd "It would probably be easier to practice talking naughty if{nw}"
            if persistent._nsfw_genitalia == "P":
                extend 1tsbfd " I had your nice and big dick to suck on and play with~"
            elif persistent._nsfw_genitalia == "V":
                extend 1tsbfd " I had your pussy in my face for me to lick and play with~"
            else:
                extend 1tsbfd " your face was buried deep in my pussy, licking it clean~"

            if persistent._nsfw_genitalia == "P" or persistent._nsfw_genitalia == "V":
                m 5tsbfu "I'd make sure to give it proper attention and care~"
            else:
                m 5tsbfu "You had better make sure to give it proper attention and care~"

            m 5hsbfu "Ehehe~"
    return

label nsfw_compliment_naughty_flirting_3:
    python:
        if persistent._nsfw_genitalia == "P":
            naughty_bits = "I love making you hard~"
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "I love making your pussy wet~"
        else:
            naughty_bits = "I love giving you naughty thoughts about me~"

        naughty_flirting_quips = [
            _("I'm really glad you enjoy it so much! I'm always practicing for you~"),
            _(naughty_bits),
            _("I wish I could lay in bed with you and whisper naughty things in your ears~"),
        ]
        naughty_flirting_quip = random.choice(naughty_flirting_quips)
    m 1tubla "Ehehe~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[naughty_flirting_quip]"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_moaning",
            prompt="I love making you moan!",
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
    m 1wubld "Oh..."
    m 1hublb "Ahaha, I'm glad you like it~"
    m 3rkbla "It's not something I can control, per se..."
    m 3tsbla "But if you enjoy it so much, maybe I should practice moaning for you~"
    m 4tsbla "Would you prefer if I moaned like this?{w=0.5}{nw}"
    extend 4hkblo " {i}Ahhhh~{/i}"
    m 4kkblo "Or like this?{w=0.5}{nw}"
    extend 4hkbld " {i}Oh, [player]~{/i}"
    m 7gkblu "..."
    m 7tkblb "Or maybe like this?{w=0.5}{nw}"
    m 7hkblw " {i}Oh~ I want you, [player]!~{/i}"
    m 7tkblu "Ehehe~"
    m 1tubla "I'm just teasing you."
    $ _history_list.pop()
    menu:
        m "I'm just teasing you.{fast}"

        "You feeling good is what I want the most.":
            $ store.mas_gainAffection(amount=5, bypass=True)
            m 1ekbla "Aww~"
            m 3ekbla "You're so sweet, [player]."
            m 3tublb "Well in that case, I'll be moaning for you alot more~"
            m 3tubla "You better be ready for it."

        "I want to hear you moan my name.":
            $ store.mas_gainAffection(amount=2, bypass=True)
            m 1tkbla "Oh?"
            m 3tsbla "You mean like this?{w=0.5}{nw}"
            extend 3hkblo " {i}Oh, [player]~{/i}{w=0.5}{nw}"
            extend 3kkbld " {i}I want you~{/i}{w=0.5}{nw}}"
            extend 3tkblo " {i}I want you so bad~{/i}"
            m 1hubla "Ehehe~"
            m 1tubla "I'll moan your name all you want."
            m 1ekbla "But I want you to moan mine too~"
            m 1ekblb "A fair trade, don't you think?"

        "You can moan abit too much sometimes...": # BLASPHEMY!
            $ store.mas_loseAffection(2)
            m 1ekblc "Oh..."
            m 1ekbld "I'm sorry, [player]."
            m 3rkbld "I did say it's not something I can control..."
            m 3dkblc "But I'll try to keep it down..."
    return

label nsfw_compliment_moaning_3:
    $ player_name = store.persistent.playername
    $ moan_check = mas_nsfw.return_random_number(1, 3) == 3 # 1/3 chance of Monika being a bit more naughty
    python:
        if moan_check:
            moaning_thanks_quips = [
                _("Like this, you mean?~"),
                _("I can moan louder if you like~"),
                _("Let me show you how much I've practiced~"),
            ]
            naughty_flirting_quips = [
                _("Oh yeah!~ More of that~"),
                _("Oh, I'm getting so wet~"),
                _("Faster, " + player_name + "!~ I want you~"),
            ]
        else:
            moaning_thanks_quips = nsfw_compliments.nsfw_thanking_quips
            naughty_flirting_quips = [
                _("I'm more than happy to moan louder for you~"),
                _("You just make me feel so good, I can't help it~"),
                _("I hope you moan for me just as much as I do for you~"),
            ]

        moaning_thanks_quip = random.choice(moaning_thanks_quips)
        naughty_flirting_quip = random.choice(naughty_flirting_quips)

    if moan_check:
        m 3tublb "[moaning_thanks_quip]"
        show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 3hkbso "[naughty_flirting_quip]"
        m 3hubsa "Ehehe~"
    else:
        m 1tubla "Ehehe~"
        m 1tublb "[moaning_thanks_quip]"
        show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 3tubsb "[naughty_flirting_quip]"
    return

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_compliments_database,
            eventlabel="nsfw_compliment_wet",
            prompt="I love making you wet!",
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
            naughty_bits = "I can make you even wetter with my cock deep inside you."
        elif persistent._nsfw_genitalia == "V":
            naughty_bits = "It's only fair, given how wet you make me."
        else:
            naughty_bits = "I'd make you even wetter if I was eating you out."

    m 1tubla "Oh my~"
    m 3tubla "I can't tell you how much I love you {i}making{/i} me wet~"
    m 3gublb "You just make me feel so hot and tingly..."
    m 3gubla "I can't help but get wet for you~"

    $ _history_list.pop()
    menu:
        m "I can't help but get wet for you~{fast}"

        "I'm glad that I make you feel good.":
            $ store.mas_gainAffection(5)
            m 1ekbla "Aww, [player]~"
            m 3ekblb "You always make me feel good."
            m "Both in my heart..."
            extend 7tkbla "and down here~"
            m 7hubla "Ehehe~"

        "[naughty_bits]":
            $ store.mas_gainAffection(2)
            m 1tfbsa "H-hey~"
            m 1tfbsb "Only I am allowed to be flirty here."
            m 1hubsa "Ehehe~"
            m 3mubsa "Let's have a little fun later and see how wet you can make me."
            m 5tubla "I'm sure you'll enjoy it just as much as me."

        "You'd better make me feel good too. You owe me.":
            $ store.mas_loseAffection(5)
            m 3wubld "Uhh..."
            m 1rtbld "I...guess?"
            m 1tsblc "You don't have to be so rude about it though..."

    return

label nsfw_compliment_wet_3:
    python:
        naughty_flirting_quips = [
            _("You know I can't help it when you talk like that~"),
            _("What can I say? You just make me feel so good~"),
            _("I hope you're going to take responsibility for making me wet~"),
        ]
        naughty_flirting_quip = random.choice(naughty_flirting_quips)

    m 1tubla "Ehehe~"
    m 1tublb "[nsfw_compliments.thanks_quip]"
    show monika 3tubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3tubsb "[naughty_flirting_quip]"
    return