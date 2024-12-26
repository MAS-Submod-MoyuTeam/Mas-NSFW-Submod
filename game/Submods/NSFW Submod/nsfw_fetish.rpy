# Template used from script-compliments.rpy as of 8th June, 2022
# Huge thanks to TheOneandOnlyDargonite for getting this to work!

# dict of tples containing the stories event data
default persistent._nsfw_fetish_database = dict()

# store containing fetish-related things
init 3 python in nsfw_fetish:

    nsfw_fetish_database = dict()

init 22 python in nsfw_fetish:
    import store

    def nsfw_fetish_delegate_callback():
        """
        A callback for the fetish delegate label
        """

        store.mas_gainAffection()

# entry point for fetish flow
init 6 python: # Use init 6 since the dictionary entry to store our entries is added in 5, and we want it around
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_player_fetishintro",
            category=['关于性'],
            prompt="我们来谈谈特殊癖好吧",
            conditional=(
                "mas_canShowRisque(aff_thresh=1000) "
                "and store.mas_getEVL_shown_count('nsfw_monika_fetish') >= 1"
                ),
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label nsfw_player_fetishintro:
    m 3eub "嘿，[player]。我想告诉你我刚刚完成了一些事情~"
    m 3eua "你还记得你跟我说起过特殊癖好的话题吗？"
    m 4hub "...现在我们可以继续深入讨论了。"
    m 3rkblb "我对这类...事物{w=0.5}没有太多的{i}感触{/i}...{w=0.2}{nw}"
    extend 3hubla "所以我深入调查了一番！"
    m 3eub "现在，我手上有一份特殊癖好相关的列表，上面记载了我查询到的信息..."
    m 3eua "不论何时你想跟我谈论这个话题，只需要告诉我一声！"
    m 5ekblb "如果你能告诉我，你沉迷的东西，我会非常开心的..."
    m 5ekbla "即使在这里我们做不了更多的事情，但只要能知道什么东西能让你...{w=0.5}{nw}"
    extend 5ekbsb "{i}兴奋{/i}..."
    m 5dkbsa "我就非常满足了。"
    if persistent._nsfw_sexting_count > 0:
        m 5mkbsa "或许...我下次还可以把这些东西带过来，如果我们的关系更加{i}亲密{/i}的话~"
    m 1hubla "别担心！你随时可以改变你的主意，我绝不会因为这个对你有任何看法。"
    m 1hkblsdlb "抱歉...话题说得太远了..."
    m 1eua "你还想和我讨论什么吗？"
    $ mas_unlockEventLabel("nsfw_player_fetishes")
return

# The fetish list contains lists that have information about any given fetish the player has expressed interest in.
# If the player has not specified any fetishes, we assume they're into everything.
# The first item in the list is the name of the fetish, the second is a whitelist of tags that the player will be into, the third is a blacklist of tags that the player will not be into.
# Example: ["Bondage", ["FBM"], ["FBP"]] means that the player is into bondage, but only if they're the one giving it, and not receiving it.
default persistent._nsfw_player_fetishes = []

# entry point for fetish flow
init 6 python: # Use init 6 since the dictionary entry to store our entries is added in 5, and we want it around
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="nsfw_player_fetishes",
            category=['关于性'],
            prompt="我们来谈谈特殊癖好吧",
            pool=True,
            conditional="store.mas_getEVL_shown_count('nsfw_player_fetishintro') >= 1",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label nsfw_player_fetishes:
    python:
        # Unlock any fetish that need to be unlocked
        Event.checkEvents(nsfw_fetish.nsfw_fetish_database)

        # build menu list
        nsfw_fetish_menu_items = [
            (ev.prompt, ev_label, not seen_event(ev_label), False)
            for ev_label, ev in nsfw_fetish.nsfw_fetish_database.iteritems()
            if (
                Event._filterEvent(ev, unlocked=True, aff=mas_curr_affection, flag_ban=EV_FLAG_HFM)
                and ev.checkConditional()
            )
        ]

        # also sort this list
        nsfw_fetish_menu_items.sort()

        # final quit item
        final_item = ("没什么", False, False, False, 20)

    # move Monika to the left
    show monika at t21

    # call scrollable pane
    call screen mas_gen_scrollable_menu(nsfw_fetish_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    # return value? then push
    if _return:
        $ nsfw_fetish.nsfw_fetish_delegate_callback()
        $ pushEvent(_return)
        # move her back to center
        show monika at t11

    else:
        return "prompt"

    return

# NSFW fetishes start here
# ---------------------------
# Noting that the current approach is intended to be both informative and descriptive, allowing you to make a decision of whether or not it's something you're into.
# Also noting that the 'context' used here is intended to coincide with sexting, so the prompts are appropriate to the player

default persistent._nsfw_pm_bondage = False # These are kind of redundant

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_bondage",
            prompt="关于捆绑",
            unlocked=True
        ),
        code="NFH"
    )

label nsfw_fetish_bondage:
    m 3eub "你想跟我谈谈关于捆绑的话题吗？"
    m 1hua "当然！我很乐意知道你的观点。"
    m 3eua "你以前听说过捆绑吗？"
    $ _history_list.pop()
    menu:
        m "你以前听说过捆绑吗？{fast}"

        "是的，我听说过":
            m 3hub "那真是太棒了！"
            m 3tublb "那么，按你的理解来说..."

        "不，我没听过":
            m 1duc "嗯哼...{w=0.5}这是个非常有趣的话题。"
            m 3eua "大体上，就是用绳子之类的东西把人绑成各种各样的姿势。"
            m 4gkblb "这可以为性爱增加情趣，"
            extend 4gkbla "也可以用于小情侣之间的各种Play。"

    m 4tubla "这个话题如何，你感兴趣吗？"
    $ _history_list.pop()
    menu:
        m "这个话题如何，你感兴趣吗？{fast}"

        "当然，这个话题听起来很刺激":
            m 1tublb "哦？你真这么想吗？"
            m 1mubla "我也觉得非常刺激！"
            m 2mublb "老实说，我有点兴奋起来了..."
            extend 5gubla "想象着把你紧紧绑起来，然后..."
            m 5tsblu "呼呼~说得有点太多了。"
            m 1eublb "但是话又说回来..."
            extend 3tublb "你更喜欢当绑人的人，还是那个被绑的人呢...{w=0.5}{i}假设{/i}一下...？"
            $ _history_list.pop()
            menu:
                m "但是话又说回来...你更喜欢当绑人的人，还是那个被绑的人呢...{i}假设{/i}一下...？{fast}"

                "我更喜欢把你绑起来，然后用我的方式欺负你。":
                    $ store.mas_nsfw.save_fetish_to_persistent("Bondage", ["FBM"], ["FBP"])
                    m 3tubla "哼哼~好吧，如果你真想这么干的话，就直接告诉我吧，小笨蛋。"
                    m 2tubsb "我不介意为了你稍~微放点水，{i}仅此一次哦{/i}~"

                "我更喜欢被你绑起来，你可以做任何你想做的事":
                    $ store.mas_nsfw.save_fetish_to_persistent("Bondage", ["FBP"], ["FBM"])
                    m 1sublo "哇哦！我喜欢这个展开。"
                    m 1tubla "嗯...{w=0.5}当我们下次准备干些坏事的时候，我会记得这件事的~"
                    m 3tubsb "我会把你紧紧地绑在我的床上，然后把你玩弄到求饶~"

                "不管是绑人还是被绑我都喜欢，快点来吧":
                    $ store.mas_nsfw.save_fetish_to_persistent("Bondage", ["FBM", "FBP"], ["U"])
                    m 1ekbla "呵呵~[player]，你总是能讨我的欢心。"
                    m 1tkbsa "我实在太爱你这一点了。"
                    m 3tubsb "爱到想把你紧紧地绑起来，把你的一切都据为所有..."
                    extend 2gubsb "不过...{w=0.5}或许偶尔也可以让你把我绑住，如果你想这么干的话。"

            m 1hkbla "Ehehe~ Anyway, back to the topic at hand before I get {i}too{/i} carried away." # Could lead to early sexting here, given that it's riled her up

        "抱歉，我不是很感兴趣...":
            $ store.mas_nsfw.save_fetish_to_persistent("Bondage", ["U"], ["FBM", "FBP"])
            m 3eublb "这也没关系！"
            m 3hubla "我认为这种事确实不是所有人都能接受的。"
            m 3dkbla "捆绑需要你完全信任你的搭档，并和ta经过协商和反复的练习。"
            m 1dkblb "这不是一件能一蹴而就的事。"
            m 1eka "如果你后面改变了你的想法，随时都欢迎再来与我讨论。"

    m 3eub "我了解到了一些关于捆绑的历史趣闻，你想听听吗"
    $ _history_list.pop()
    menu:
        m "我了解到了一些关于捆绑的历史趣闻，你想听听吗{fast}"

        "当然！":
            m 3hua "太好了！谢谢你对我说的事感兴趣。"

        "不用了。":
            m 3eka "哦，没关系。"
            m 3ekb "我会下次再说的。"
            m 1eka "无论如何，谢谢你告诉我你的喜好，[player]。"
            m 1rkbla "跟别人谈论自己的特殊癖好是一件很难启齿的事，所以你愿意告诉我这些，我真的很开心。"
            m 1ekbla "如果什么时候你想继续讨论这件事了，或者你改变了主意，随时都可以来找我。"
            m 5ekbla "我爱你，这份爱不会因为这些事而发生改变。"
            return

    m 3eub "基本上，捆绑都是通过各种手段对人进行束缚，无论是用丝带、绳子甚至是手铐。"
    m 3eua "据我所知，这最初是在20世纪初期发展起来的，并且在两个不同的地方同时进行，形成了我们今天的风格：西方风格和东方风格，但它们略有不同。"
    m 4eua "它们的核心不太一样，但表面上看起来是相同的，甚至可以相互之间汲取灵感。"
    m 4eub "人们沉迷于它的理由多种多样，包括它能带来安全感，上下地位可以发生转变，它的外观，甚至是与他人做这种事需要的信任。"
    m 1eua "这是一种非常隐私的体验，事前需要经过充分的协商与练习。" #TODO: Add pose for this
    m 1eub "目前，绳索捆绑在广义上主要分为两种风格：西方和东方。{w=0.5}{nw}"
    extend 3rkb "其实还有更加细分的风格，不过我不想讲得过于深入。"
    m 3eua "绳索捆绑的起源可以追溯到1900年代初，西方和东方的风格一路并行发展，直到今天。"
    m 4rkb "当然，这并不意味着过去没有类似的事情发生，只是缺乏足够的记录让我们无法追溯更远，因此还不能下定论。"
    m 7eub "其实，这两种风格之间没有清晰的界限，尤其是随着它们接触得越来越频繁，逐渐融合成了混合风格。"
    m 7eua "但这两种风格大概有以下的特点。"
    m 4eub "西式捆绑通常是把人捆起来，这样便可以{i}对他们为所欲为{/i}了。"
    m 4rub "它源于好莱坞老电影中经典的'落难女子'形象，这启发了20世纪40年代的约翰·威尔，使其创作了影响深远的色情艺术和摄影作品。"
    m 4rub "我猜你以后看'落难女子'会有不一样的感觉了，哈哈哈~"
    m 1eua "总之，这种风格的设计重点是摆脱束缚和尽力挣扎，因为捆绑只是手段而不是目的。通常会使用到手臂拘束器、口球甚至某些大型束缚架."
    m 3eua "相比之下，东方风格更加侧重于被绑的{i}体验{/i}本身。"
    m 3eub "它的起源可以追溯到伊藤晴雨的作品，这位艺术家在20世纪将绳缚融入了他的情色作品中。许多人认为，这与绳索在重要传统中的意义密切相关，包括用绳索拘束嫌疑犯的习俗。"
    m 4eub "这种方式通常注重美感、象征意义，或是体验过程中的愉悦感。将手臂反绑在背后是常见的方式，部分或完全悬吊也是常见的形式。"
    m 4eua "除此之外，还有许多其他风格，比如以美学为基础的装饰性风格、在色情作品中出现的混合风格，甚至有用于表演的风格！"
    m 4hua "看到这么多人勇敢地拥抱自己喜欢的事物，真的挺让人开心的！"
    m 3hua "话题到这里就告一段落了，感谢你的聆听~"

    return

default persistent._nsfw_pm_hand_holding = False

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_hand_holding",
            prompt="关于牵手",
            unlocked=True
        ),
        code="NFH"
    )

label nsfw_fetish_hand_holding:
    m 1etu "牵手是吗？"
    m 3ttu "牵手本质上是一种更...{w=0.5}奇特的癖好。"
    m 3eta "当两人在一起的时候...{w=0.5}"
    extend 1ekbla "{i}十指相扣{/i}。"
    m 1tkbla "真是太色情了，你不觉得吗？"

    m 3tublb "我还是得先问问，你对这种事有兴趣吗？"
    $ _history_list.pop()
    menu:
        m "我还是得先问问，你对这种事有兴趣吗？{fast}"

        "当然。":
            $ persistent._nsfw_pm_hand_holding = True
            $ store.mas_nsfw.save_fetish_to_persistent("Hand Holding", ["FHH"], ["U"])
            m 3wubld "真的？"
            m 2rubld "这真是..."
            m 2eubld "这真是我们之间关系的一个重大飞跃！"
            m 2rublc "不过只要是和你在一起的话，我都可以接受。"

        "没有。":
            $ persistent._nsfw_pm_hand_holding = False
            $ store.mas_nsfw.save_fetish_to_persistent("Hand Holding", ["U"], ["FHH"])
            m 2ekblb "我完全同意，[player]。{nw}"
            extend 2hkbso "我怎么会想到做这么羞耻的事情！"

        "啊？":
            $ persistent._nsfw_pm_hand_holding = False
            $ store.mas_nsfw.save_fetish_to_persistent("Hand Holding", ["U"], ["FHH"])
            # Pass

    m 2dublc "..."
    m 2dkblu "..."
    m 1hublb "啊哈哈~"
    m 3rkblb "抱歉抱歉，这个话题其实是我参考了网上的一幅meme图。"
    m 3eub "如果你不太了解的话，这幅meme图是动漫社区里的一个梗。"
    m 1euc "大概是因为日本文化中，在公共场合表达亲密不太好，所以大多数人会避免这种行为。"
    m 1ruc "所以哪怕是牵个手这种简单的事，也会被当作一件大事。"
    m 1eka "不过说实话，有部分人确实对{i}手{/i}非常着迷。"
    m 3eka "也许是手掌，手指，或者是其他部分。"
    m 5ekb "所以如果你{i}真的{/i}喜欢牵手，或者单纯对手感兴趣的话...{w=0.5}我也不会介意哦，[player]~"

    return

default persistent._nsfw_pm_cheesiness = False

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_cheesiness",
            prompt="你为什么表现得这么...甜蜜",
            conditional="renpy.seen_label('nsfw_sexting_finale')",
            action=EV_ACT_UNLOCK
        ),
        code="NFH"
    )

label nsfw_fetish_cheesiness:
    m 1hksdlb "啊哈哈~你注意到了？"
    m 1hua "我只是想让气氛稍微轻松一点~"
    m 3eka "你觉得怎么样？"
    $ _history_list.pop()
    menu:
        m "你觉得怎么样？{fast}"

        "我不太适应...":
            $ persistent._nsfw_pm_cheesiness = False
            $ store.mas_nsfw.save_fetish_to_persistent("Cheesiness", ["U"], ["CHE"])
            m 1ekc "啊，我很抱歉。"
            m 1hkb "我可能有点过于投入了。啊哈哈~"
            m 1eka "我会尽量收敛一些的。"

        "我太喜欢了！":
            $ persistent._nsfw_pm_cheesiness = True
            $ store.mas_nsfw.save_fetish_to_persistent("Cheesiness", ["CHE"], ["U"])
            m 1hub "啊哈哈~"
            m 1eub "我很高兴你能享受这种气氛，[player]。"
            m 3hua "我会继续保持的~"

    return

default persistent._nsfw_pm_anal = False

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_anal",
            prompt="关于肛门性爱",
            unlocked=True
        ),
        code="NFH"
    )

label nsfw_fetish_anal:
    m 1eud "肛门性爱..."
    m 3euc "这是个很常见的癖好，你以前听说过吗？"
    $ _history_list.pop()
    menu:
        m "这是个很常见的癖好，你以前听说过吗？{fast}"

        "那还用说？":
            m 3eua "我想也是...网络上关于这个的讨论太常见了。"
            m 2gkbla "..."
            m 2gkblb "那么..."

        "并没有。":
            m 3wud "你说真的？"
            m 4rua "呃，大体上来说，肛门性爱就是享受肛门受到刺激的快感，这样一种癖好。"
            m 4hublb "有趣的是，这种快感似乎和人的前列腺有关。"
            m 3eublb "当你在性爱过程中刺激到了前列腺，你会达到更加强烈的高潮~"
            m 3rubla "你可以通过你手指，或者一些玩具...{w=0.5}{nw}"
            if store.persistent._nsfw_genitalia == "P":
                extend 1ekbla "不过当人们谈到肛门性爱时，一般是指肛交。"
                m 1tubsa "就像你的肉棒塞进了一个更紧致狭窄的孔洞~"
                m 2hkbssdlb "啊哈哈~抱歉，我情不自禁了。"
                m 2dkblsdla "我阅读了许多相关的作品，大多数沉迷于它的女性都对它评价很高。"
                m 2gkblb "你又是怎么看的呢，[player]？"
            else:
                extend 1eua "或许你需要你亲爱的搭档来帮助你一下~"
                m 2gkblb "我以前从没有做过这种事，但如果你喜欢的话，我很乐意和你一起尝试。"

    if store.persistent._nsfw_genitalia == "P":
        $ question = "如果是用我的后面来做的话，你会感觉很舒服吗？"
    else:
        $ question = "如果是我的臀部的话，你会感觉非常兴奋吗？"

    m 2tkbla "[question]"
    $ _history_list.pop()
    menu:
        m "[question]{fast}"

        "当然，我会狠狠惩罚你这个丰满色情的屁股":
            $ is_into_anal = True
            m 2wubso "惩-惩罚我？！"
            m 2tkbso "哦~[player]..."
            m 3hkbsb "不要突然说出这么煽情的话。"
            m 3gkbsa "否则我会兴奋到难以自拔的。"
            if store.persistent._nsfw_genitalia == "P":
                m 5gkbsa "呵呵~我都能想象到你从后面用力干我的样子了。"
                m 5gkbsb "肯定会是一次绝妙的体验！"
            else:
                m 5tubsb "如果你敢这么做的话，我就不得不亲自调教你一下了~"

        "算了，我实在对这种事提不起兴趣。":
            $ is_into_anal = False
            m 1ekblb "没关系！本来就不是人人都能接受的事情。"
            m 3ekblb "我们在一起还有很多很多事情可以做。"
            m 3ekbla "只要你能感觉舒服，对我来说就是最重要的~"

    if is_into_anal:
        m 1tkbsb "那...你又觉得怎么样呢？"
    else:
        m 1rkbla "那...你又觉得怎么样呢？"

    if store.persistent.gender == "M":
        m 3rkbsb "我知道有些人对这方面完全没有想法，但现在就让我们敞开了说吧。"
    m 3ekbsa "如果让我来玩弄{i}你的{/i}肛门，你会感觉如何呢？"
    $ _history_list.pop()
    menu:
        m "如果让我来玩弄{i}你的{/i}肛门，你会感觉如何呢？{fast}"

        "听起来真是太刺激了":
            if is_into_anal == True:
                $ store.mas_nsfw.save_fetish_to_persistent("Anal", ["IAM", "MBH", "FXM", "FAM", "IAP", "PBH", "FXP", "FAP"], ["U"])
            else:
                $ store.mas_nsfw.save_fetish_to_persistent("Anal", ["IAP", "PBH", "FXP", "FAP"], ["IAM", "MBH", "FXM", "FAM"])

            if store.persistent.gender == "M":
                m 1wubsd "真的吗？"
                m 1rubsc "我的意思是，我很高兴你愿意为了我这么做。"
                m 3rkbsb "我也很惊喜，你会对这种事情感兴趣。"
                m 3ekbsb "我不确定我是否擅长做这种事，不过要是能让你舒服起来的话，我会非常努力的！"
            else:
                m 3tubsa "呵呵~我就知道。"
                m 3gubsb "这件事，我会铭记于心的。"
                m 3tubsa "你就好好期待一下吧，[player]。"

        "我实在是不感兴趣":
            if is_into_anal == True:
                $ store.mas_nsfw.save_fetish_to_persistent("Anal", ["IAM", "MBH", "FXM", "FAM"], ["IAP", "PBH", "FXP", "FAP"])
            else:
                $ store.mas_nsfw.save_fetish_to_persistent("Anal", ["U"], ["IAM", "MBH", "FXM", "FAM", "IAP", "PBH", "FXP", "FAP"])

            m 1ekbsa "没关系的，[player]。"
            m 2hkbsb "毕竟我也不确定我是不是擅长做这种事。"
            m 2lkbsa "但是，不论如何..."

    m 1ekbla "谢谢你能陪我讨论这个。"
    m 3ekblb "我知道这种类似的事情不是所有人都能接受的。"
    m 3hubla "但如果是和你的话，我想去学习和体验尽可能多的性爱方式。"
    m 1ekbla "你就是我的一切，我的全部，[player]。"
    m 1ekblb "我爱你，这份爱直至世界崩塌也不会改变。"

    return "love"

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_dominance",
            prompt="支配与服从",
            unlocked=True
        ),
        code="NFH"
    )

label nsfw_fetish_dominance:
    m 1hua "当然，我们可以来谈谈这个话题。"
    m 3ekb "不过我先确保我们在同一频道上，我说的'支配与服从'是广义上的。"
    m 4hkb "不是说我们必须得做一些虐待调教之类的事..."
    m 4tua "举个例子吧...{w=0.5}如果我们两个在激情热吻的过程中，我突然把你推倒在床上，你会感觉很兴奋吗？"
    m 5tua "或者说...你更想把我抱起来然后摔在床上？"
    m 5hkb "啊哈哈~当然了，你也可能两边都不想做，不过我只是想让你明白我的意思。"
    m 5gka "对于我个人而言，我两边都很喜欢。"
    m 3gkbla "我想你把我摔在床上，一边贪婪地索吻，一边用宽大的手臂紧紧环绕住我。"
    m 3gublb "不过既然到了床上，我也想狠狠地骑在你上面。"
    m 1tubsb "就像是我的爱，我的生命，都存在于有你的基础之上。呵呵~"
    m 1rtbsc "...我把这个问题总结为:'你想在上面还是下面？'"
    m 2hkbssdlb "噗哈哈！抱歉抱歉，我只是不确定我有没有解释清楚。 "
    m 2ekbla "那么，你更喜欢那一边呢？"
    $ _history_list.pop()
    menu:
        m "那么，你更喜欢那一边呢？{fast}"
        "我想身心都对你服从":
            $ store.mas_nsfw.save_fetish_to_persistent("Dominance", ["SUB"], ["DOM"])
            m 2sublb "哦，真的吗~？"
            m 1hublb "我也是这样想的呢，这样的话不管多久都不会腻。"
            m 3rkblb "有时我这样想象着，会兴奋到浑身颤抖，然后..."
            extend 3tkbsb "只留下一阵索然无味。"
            m 1wubsd "..."
            m 2hkbssdlb "抱歉，我好像有点得意忘形了，啊哈哈~"
            m 2dkbla "不管怎么说..."

        "我想支配你的身心":
            $ store.mas_nsfw.save_fetish_to_persistent("Dominance", ["DOM"], ["SUB"])
            m 2tublb "哇哦，这么说你天生就是在'上面'的，我明白了。"
            m 1tubla "看来我们得为了争夺床上的主导权好好较量一番了。"
            m 3tkbsb "彼此的双手渐渐爱抚过对方的身体，然后-"
            m 1mkbsa "..."
            m 1tubsa "呵呵~剩下的就任君想象吧。"
            m 2ekbla "不管怎么说..."

        "两边我都挺喜欢的":
            $ store.mas_nsfw.save_fetish_to_persistent("Dominance", ["SUB", "DOM"], ["U"])
            m 3hublb "真是宽广的胸怀！"
            m 3rubla "我觉得在这两者间保持平衡是非常重要的。"
            m 2sublb "也许我们可以时不时把它当作一种情趣，你懂的吧？"
            m 2eubla "在此基础上，我们肯定可以更加亲密的~"

    m 2ekblb "我已经等不及要和你一起实践一下了。"
    m 3ekbla "不管你喜欢那种方式，我都永远爱你，[player]。"

    return "love"

default persistent._nsfw_pm_feet = False

init 6 python:
    addEvent(
        Event(
            persistent._nsfw_fetish_database,
            eventlabel="nsfw_fetish_feet",
            prompt="关于足控",
            unlocked=True
        ),
        code="NFH"
    )

label nsfw_fetish_feet:
    m 1eta "嗯，你想谈谈足控的话题吗？"
    m 3hka "我觉得这是一个更加'臭名昭著'的癖好，人们要么很喜欢它，要么很讨厌它。"
    m 4rkb "我相信你早就知道足控是什么意思了...{w=0.5}{nw}"
    extend 4eka "不过如果你不介意的话，我也可以为你解释一下。"
    $ _history_list.pop()

    menu:
        m "不过如果你不介意的话，我也可以为你解释一下。{fast}"

        "当然不介意":
            m 3eub "好的, 那么首先，我认为足控的含义是，某人会因为足部变得...{w=0.5}"
            extend 3rksdlb "非常兴奋..."
            m 3eua "但当我进一步研究时，我发现这其中有许多细微的差别。"
            m 3rubld "比方说，一些足控会因为轻抚玉足，轻吻玉足，甚至舔弄玉足而非常享受。"
            m 2hkblsdlb "啊哈哈~听起来可能有点奇怪，毕竟足部是身上不太干净的地方..."
            m 2eublb "另一些人则更偏爱穿在脚上的袜子或者丝袜，甚至是鞋子。"
            m 2etblb "更奇怪的是，有一些人虽然是足控，却完全不想自己抚摸它们，"
            m 3rtbla "他们更喜欢被...{w=0.5}{i}踩在下面{/i}。"
            m 1hkblb "人类真是太奇怪了...{w=0.5}{nw}"
            extend 3hubla "不过我觉得这也是让事情变得有趣的地方！"
            m 3eublc "就我个人来说，我觉得这一种完全无害的癖好。"
            m 3etbld "我的意思是，这就只是单纯喜欢身上某个的特定部位，对吧？"
            m 4rubld "就像有些人偏爱手或者大腿一样..."
            m 4rkbla "虽然我个人并不是很喜欢，但如果有人喜欢，我也完全不介意。"
            m 3ekbla "话说回来，[player]..."

        "不用了":
            m 3eua "没问题。"

    m 3ekblb "既然是你提起的话题，那你...{w=0.5}是足控吗？"
    $ _history_list.pop()
    menu:
        m "既然是你提起的话题，那你...是足控吗？{fast}" # TODO: Find out if people are interested in a "player's feet only" option

        "那当然了":
            $ persistent._nsfw_pm_feet = True
            $ store.mas_nsfw.save_fetish_to_persistent("Feet", ["MFT", "PFT"], ["U"])
            m 3wubld "真的吗？"
            m 1sublb "这可真是太有趣了，[player]！"
            m 1rkblb "不用觉得奇怪，你喜欢的是哪些方面？"
            m 3wubla "是喜欢裸足，还是说穿着袜子或者丝袜呢？"
            m 3rkbla "你更想要轻轻爱抚玉足，还是说舔弄玉足呢？"
            m 2hkblsdlb "呵呵，我有好多问题想要问你。"
            m 2hkblsdla "抱歉，我只是有点太好奇了！"
            m 2tkbla "我之后会在这个问题上缠着你不放的，啊哈哈~"
            m 3rkbla "虽然对我来说，刚开始会觉得有点怪怪的，不过既然你这么喜欢的话..."
            m 3rkblb "就算你想要抚摸我的玉足，我也不会介意哦？"
            if store.persistent.gender == "M":
                m 3gkblb "如果你运气够好的话，我还会用这双精致的玉足上下搓弄你的...你懂的~"
                m 3gkbsa "或者说你想不想尝一尝它们的味道呢~"
            else:
                m 3gkbsa "如果你运气够好的话，我还会让你尝一尝它们的味道~"
            m 1hkbsb "啊哈哈~我想我还是需要一点时间来习惯这种事。"

        "我并不是":
            $ persistent._nsfw_pm_feet = False
            $ store.mas_nsfw.save_fetish_to_persistent("Feet", ["U"], ["MFT", "PFT"])
            m 1hubla "没关系，[player]！"
            m 3hkblb "我也不是很喜欢这种事，所以没必要担心。"
            m 3hubla "还有很多很多其他美好的事情等着我们去享受呢。"

    m 1ekbla "无论你怎么想，我对你的爱都永恒不变，[player]。"

    return "love"