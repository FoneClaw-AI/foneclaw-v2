"""i18n module — manages translations and hreflang tags for FoneClaw multi-language support."""

# Supported languages
LANGUAGES = {
    'en': {'name': 'English', 'native': 'English', 'dir': ''},
    'zh': {'name': 'Chinese (Simplified)', 'native': '简体中文', 'dir': 'zh'},
    'tw': {'name': 'Traditional Chinese (Taiwan)', 'native': '繁體中文', 'dir': 'tw', 'hreflang': 'zh-TW'},
}

# Translation dictionaries — keyed by page
# Structure: {lang: {page: {key: translated_text}}}

TRANSLATIONS = {
    # ═══════════════════════════════════════════
    # HOMEPAGE
    # ═══════════════════════════════════════════
    'homepage': {
        'meta_title': {
            'en': 'FoneClaw - Android AI Phone Assistant | 120+ Voice Actions',
            'zh': 'FoneClaw - Android AI手机助手 | 120+ 语音操作',
        },
        'meta_desc': {
            'en': 'FoneClaw is the Android AI agent that controls your phone by voice. 120+ actions across 16 categories: device health, messages, settings, screenshots, navigation, and more.',
            'zh': 'FoneClaw 是通过语音控制手机的 Android AI 智能助手。16 大类 120+ 操作：设备状态、消息、设置、截图、导航等。',
        },
        'hero_slogan': {
            'en': 'Say it. Done.',
            'zh': '说出来，就搞定。',
        },
        'hero_lead': {
            'en': '120+ phone actions, one voice command. Free to use. FoneClaw is the Android AI agent that actually controls your phone — not just answers questions.',
            'zh': '一条语音指令，完成 120+ 手机操作。核心功能免费。FoneClaw 是能帮你实际操作 Android 手机的 AI 助手，不仅仅是语音助手。',
        },
        'cta_download': {
            'en': 'Download APK',
            'zh': '下载 APK',
        },
        'cta_copy': {
            'en': 'Download free. Get the latest Android build.',
            'zh': '免费下载，获取最新 Android 安装包。',
        },
        'cta_see_features': {
            'en': 'See Features →',
            'zh': '查看功能 →',
        },
        'scenario_title': {
            'en': 'Three things your phone should do for you',
            'zh': '你的手机应该为你做的三件事',
        },
        'scenario_desc': {
            'en': 'FoneClaw handles the everyday phone tasks that take too much of your time.',
            'zh': 'FoneClaw 帮你处理那些浪费时间的日常手机操作。',
        },
        'scenario_1_title': {
            'en': 'Daily Brief',
            'zh': '每日简报',
        },
        'scenario_1_desc': {
            'en': 'Summarize SMS, notifications, and system info by contact and time. Know what matters without scrolling through every app.',
            'zh': '按联系人和时间汇总短信、通知和系统信息。不用逐个翻应用，一眼看到重点。',
        },
        'scenario_2_title': {
            'en': 'Phone Health',
            'zh': '手机健康',
        },
        'scenario_2_desc': {
            'en': 'Check battery, storage, network, and permission risks in one voice report. No more digging through Android settings.',
            'zh': '一条语音报告，查看电池、存储、网络和权限风险。不用再翻 Android 设置。',
        },
        'scenario_3_title': {
            'en': 'Passive Triggers',
            'zh': '被动触发',
        },
        'scenario_3_desc': {
            'en': 'Take a screenshot or photo in any app, and FoneClaw auto-detects it and offers a summary. No context switch needed.',
            'zh': '在任何应用中截图或拍照，FoneClaw 自动检测并提供摘要。无需切换应用。',
        },
        'stat_categories': {
            'en': 'feature categories',
            'zh': '功能分类',
        },
        'stat_actions': {
            'en': 'supported actions',
            'zh': '支持的操作',
        },
        'stat_free': {
            'en': 'for core features',
            'zh': '核心功能',
        },
        'stat_android': {
            'en': 'system-level execution',
            'zh': '系统级执行',
        },
        'articles_title': {
            'en': 'Deep dives into FoneClaw',
            'zh': '深入了解 FoneClaw',
        },
        'articles_desc': {
            'en': 'Explore our latest guides on voice-controlled Android.',
            'zh': '探索我们最新的 Android 语音控制指南。',
        },
        'bottom_cta_title': {
            'en': '120+ actions, free to try.',
            'zh': '120+ 操作，免费试用。',
        },
        'bottom_cta_desc': {
            'en': 'Download FoneClaw and test every supported Android action with voice.',
            'zh': '下载 FoneClaw，用语音测试所有支持的 Android 操作。',
        },
        'footer_slogan': {
            'en': 'FoneClaw is the Android AI agent that actually controls your phone — not just answers questions.',
            'zh': 'FoneClaw 是能帮你实际操作 Android 手机的 AI 助手，不仅仅是语音助手。',
        },
    },

    # ═══════════════════════════════════════════
    # FEATURES PAGE
    # ═══════════════════════════════════════════
    'features': {
        'meta_title': {
            'en': 'FoneClaw Features - Android AI Phone Assistant',
            'zh': 'FoneClaw 功能介绍 - Android AI 手机助手',
        },
        'meta_desc': {
            'en': 'Explore 120+ FoneClaw features across 16 categories: phone status, messages, system settings, screenshots, email, calendar, maps, and web tasks for Android. Free to use.',
            'zh': '探索 FoneClaw 16 大类 120+ 功能：手机状态、消息、系统设置、截图、邮箱、日历、地图和 Web 任务。免费使用。',
        },
        'hero_title': {
            'en': '120+ phone actions, one voice command.',
            'zh': '一条语音指令，完成 120+ 手机操作。',
        },
        'hero_lead': {
            'en': 'FoneClaw turns Android capabilities into natural-language commands: device health, messages, settings, screenshots, navigation, and more.',
            'zh': '你可以用自然语言让 FoneClaw 操作 Android 手机：查看设备状态、整理消息、调整设置、截图、导航等。',
        },
        'cta_download': {
            'en': 'Download APK',
            'zh': '下载 APK',
        },
        'cta_copy': {
            'en': 'Download free. Get the latest Android build.',
            'zh': '免费下载，获取最新 Android 安装包。',
        },
        'cta_explore': {
            'en': 'Explore features',
            'zh': '探索功能',
        },
    },

    # ═══════════════════════════════════════════
    # FEATURES PAGE - SHOWCASE SECTIONS
    # ═══════════════════════════════════════════
    'features_showcase': {
        'cat_title': {
            'en': '16 feature categories, 120+ actions',
            'zh': '16 大功能分类，120+ 操作',
        },
        'cat_desc': {
            'en': 'Every capability is organized by what you want to do on your phone. Some features need setup; some work out of the box.',
            'zh': '每项功能按使用场景分类。部分功能需要设置，部分开箱即用。',
        },
        'cmd_title': {
            'en': 'Eight commands that show the product',
            'zh': '八条指令展示产品能力',
        },
        'cmd_desc': {
            'en': 'Each command maps to a visible phone result: health report, summary, setting change, screenshot understanding, location, or navigation.',
            'zh': '每条指令对应一个可见的手机结果：健康报告、摘要、设置变更、截图理解、定位或导航。',
        },
        'trust_title': {
            'en': 'Permissions, setup, and user control',
            'zh': '权限、设置与用户控制',
        },
        'trust_desc': {
            'en': 'FoneClaw uses Android permissions for real phone actions. Trust is part of the product experience.',
            'zh': 'FoneClaw 会在 Android 授权范围内执行手机操作。哪些权限用于哪些功能，用户应该看得清楚。',
        },
        'faq_title': {
            'en': 'Frequently asked questions',
            'zh': '常见问题',
        },
        'bottom_cta_title': {
            'en': 'Ready to try a phone assistant that can actually act?',
            'zh': '准备好试试真正能行动的手机助手了吗？',
        },
        'bottom_cta_desc': {
            'en': 'Download FoneClaw and test 120+ supported phone actions, transparent permissions, and practical everyday tasks on Android.',
            'zh': '下载 FoneClaw，免费体验 Android 9+ 上的 120+ 项手机操作。权限透明，敏感操作执行前会向你确认。',
        },
    },

    # ═══════════════════════════════════════════
    # FEATURES PAGE - SECTIONS (showcase, trust, faq, commands)
    # ═══════════════════════════════════════════
    'features_sections': {
        'eyebrow_phone': {'en': 'Phone status', 'zh': '手机状态'},
        'show1_title': {'en': 'Know what is happening on your phone.', 'zh': '了解你的手机正在发生什么。'},
        'show1_desc': {'en': 'Turn device health into an explainable report instead of digging through settings screens.', 'zh': '将设备健康状况转化为可读报告，不用再翻找设置页面。'},
        'show1_b1': {'en': 'Memory, storage, battery, and network status', 'zh': '内存、存储、电池和网络状态'},
        'show1_b2': {'en': 'App permission and sensitive-permission review', 'zh': '应用权限和敏感权限审查'},
        'show1_b3': {'en': 'Active app and hidden-app signal checks', 'zh': '活跃应用和隐藏应用信号检查'},
        'eyebrow_messages': {'en': 'Messages and notifications', 'zh': '消息和通知'},
        'show2_title': {'en': 'Turn phone noise into a daily brief.', 'zh': '将手机噪音转化为每日简报。'},
        'show2_desc': {'en': 'FoneClaw summarizes SMS, notifications, and system information so important items are not buried across apps.', 'zh': 'FoneClaw 汇总短信、通知和系统信息，重要事项不会被埋在各个应用里。'},
        'show2_b1': {'en': 'Summarize SMS by contact and time', 'zh': '按联系人和时间汇总短信'},
        'show2_b2': {'en': 'Search information by topic', 'zh': '按主题搜索信息'},
        'show2_b3': {'en': 'View context and mark items as handled', 'zh': '查看上下文并标记已处理'},
        'eyebrow_controls': {'en': 'Controls', 'zh': '控制'},
        'show3_title': {'en': 'Change Android settings faster.', 'zh': '更快地更改 Android 设置。'},
        'show3_desc': {'en': 'Use natural language for supported Android settings instead of manually navigating deep menus.', 'zh': '用自然语言操作支持的 Android 设置，不用手动翻找深层菜单。'},
        'show3_b1': {'en': 'Brightness, auto brightness, screen timeout, rotation', 'zh': '亮度、自动亮度、屏幕超时、旋转'},
        'show3_b2': {'en': 'Media, ringtone, notification, alarm, call, and system volume', 'zh': '媒体、铃声、通知、闹钟、通话和系统音量'},
        'show3_b3': {'en': 'Silent mode, Do Not Disturb, flashlight, and system setting pages', 'zh': '静音模式、勿扰模式、手电筒和系统设置页面'},
        'eyebrow_productivity': {'en': 'Productivity and navigation', 'zh': '效率和导航'},
        'show4_title': {'en': 'Move from intent to a phone result.', 'zh': '从意图到手机结果。'},
        'show4_desc': {'en': 'FoneClaw handles configured email, calendar, alarms, local notes, location, nearby search, map navigation, and web tasks.', 'zh': 'FoneClaw 处理已配置的邮箱、日历、闹钟、本地笔记、定位、附近搜索、地图导航和网页任务。'},
        'show4_b1': {'en': 'Email requires IMAP/SMTP setup', 'zh': '邮箱需要 IMAP/SMTP 配置'},
        'show4_b2': {'en': 'Maps require an installed map app', 'zh': '导航需要安装地图应用'},
        'show4_b3': {'en': 'Web comparison uses web-derived information, not guaranteed real-time prices', 'zh': '网页比价使用网络信息，不保证实时价格'},
        'eyebrow_connectivity': {'en': 'Connectivity', 'zh': '连接'},
        'show5_title': {'en': 'Control Wi-Fi and Bluetooth by voice.', 'zh': '语音控制 Wi-Fi 和蓝牙。'},
        'show5_desc': {'en': 'Manage wireless connections without digging through Android settings. Scan, connect, pair, and forget from a single command.', 'zh': '不用翻找 Android 设置即可管理无线连接。一条指令完成扫描、连接、配对和忘记。'},
        'show5_b1': {'en': 'Wi-Fi: scan nearby, connect, forget, saved networks', 'zh': 'Wi-Fi：扫描附近、连接、忘记、已保存网络'},
        'show5_b2': {'en': 'Bluetooth: pair, connect, view paired and connected devices', 'zh': '蓝牙：配对、连接、查看已配对和已连接设备'},
        'show5_b3': {'en': 'Works with headphones, speakers, cars, and wearables', 'zh': '支持耳机、音箱、汽车和穿戴设备'},
        'eyebrow_passive': {'en': 'Passive triggers', 'zh': '被动触发'},
        'show6_title': {'en': 'FoneClaw works even when you do not open the app.', 'zh': '即使不打开应用，FoneClaw 也能工作。'},
        'show6_desc': {'en': 'When you take a screenshot or photo in any app, FoneClaw can detect it and offer an instant summary in a floating window. No context switch needed.', 'zh': '在任何应用中截图或拍照时，FoneClaw 可以检测并在浮动窗口中提供即时摘要。无需切换应用。'},
        'show6_b1': {'en': 'Screenshot auto-detection and summary', 'zh': '截图自动检测和摘要'},
        'show6_b2': {'en': 'Photo auto-detection and content analysis', 'zh': '照片自动检测和内容分析'},
        'show6_b3': {'en': 'Floating window overlay, stays out of your way', 'zh': '浮动窗口覆盖层，不会干扰你'},
        'show6_b4': {'en': 'Requires detection and overlay permissions', 'zh': '需要检测和覆盖权限'},
        'trust1_title': {'en': 'Transparent permissions', 'zh': '透明权限'},
        'trust1_b1': {'en': 'Accessibility for screen reading and node actions', 'zh': '无障碍服务用于屏幕读取和节点操作'},
        'trust1_b2': {'en': 'Notification access for notification summaries', 'zh': '通知访问用于通知摘要'},
        'trust1_b3': {'en': 'Contacts, SMS, location, camera, Bluetooth, overlay, and system-setting permissions where needed', 'zh': '按需使用联系人、短信、定位、相机、蓝牙、覆盖和系统设置权限'},
        'trust2_title': {'en': 'Confirmation for sensitive actions', 'zh': '敏感操作需确认'},
        'trust2_desc': {'en': 'Dialing, sending SMS, sending email, deleting records, and other sensitive actions should require confirmation before execution.', 'zh': '拨号、发送短信、发送邮件、删除记录和其他敏感操作应在执行前要求确认。'},
        'trust3_title': {'en': 'Setup requirements are clear', 'zh': '设置要求明确'},
        'trust3_desc': {'en': 'Email needs IMAP/SMTP configuration. Navigation needs an installed map app. Screenshot/photo auto-summary needs detection and overlay permissions. Some Android settings need extra authorization.', 'zh': '邮箱需要 IMAP/SMTP 配置。导航需要安装地图应用。截图/照片自动摘要需要检测和覆盖权限。部分 Android 设置需要额外授权。'},
        'faq1_q': {'en': 'What can FoneClaw control on Android?', 'zh': 'FoneClaw 能控制 Android 的什么？'},
        'faq1_a': {'en': 'FoneClaw supports 120+ current Android phone actions across 16 categories: device checks, notification and SMS summaries, calls, system settings, Wi-Fi and Bluetooth, screenshots and photos, screen reading, email, calendar, alarms, local notes, maps, and web tasks.', 'zh': 'FoneClaw 目前覆盖 16 大类、120+ 项 Android 手机操作，包括设备检查、通知和短信摘要、通话、系统设置、Wi-Fi 和蓝牙、截图和照片、屏幕读取、邮箱、日历、闹钟、本地笔记、地图和网页任务。'},
        'faq2_q': {'en': 'Does FoneClaw need Accessibility permission?', 'zh': 'FoneClaw 需要无障碍权限吗？'},
        'faq2_a': {'en': 'Yes. Accessibility is required for screen reading, node-based clicks, notification panel operations, and some phone-level interactions that cannot be handled by standard app permissions alone.', 'zh': '是的。无障碍权限用于屏幕读取、基于节点的点击、通知面板操作以及标准应用权限无法处理的部分手机级交互。'},
        'faq3_q': {'en': 'Can FoneClaw send SMS or email automatically?', 'zh': 'FoneClaw 能自动发送短信或邮件吗？'},
        'faq3_a': {'en': 'FoneClaw can draft, prepare, and execute supported communication actions, but sensitive operations such as sending messages or email should require user confirmation before final execution.', 'zh': 'FoneClaw 可以帮你起草消息、准备内容，并执行已支持的沟通类操作；但发送短信、邮件等敏感动作，最终执行前应由你确认。'},
        'faq4_q': {'en': 'Does every feature work without setup?', 'zh': '所有功能都能免设置使用吗？'},
        'faq4_a': {'en': 'No. Email needs IMAP/SMTP setup, maps need an installed map app, image auto-summary needs the relevant detection and overlay permissions, and some Android settings require additional system permissions. Core features like phone status, SMS summary, and system settings work out of the box.', 'zh': '不是。邮箱需要 IMAP/SMTP 配置，地图需要安装地图应用，图片自动摘要需要相关检测和覆盖权限，部分 Android 设置需要额外系统权限。手机状态、短信摘要和系统设置等核心功能开箱即用。'},
        'faq5_q': {'en': 'What features are available?', 'zh': '有哪些功能？'},
        'faq5_a': {'en': 'FoneClaw covers 16 feature categories with 120+ supported actions: device checks, notification and SMS summaries, calls, system settings, Wi-Fi and Bluetooth, screenshots and photos, screen reading, email, calendar, alarms, local notes, maps, web tasks, workflows, and quick commands.', 'zh': 'FoneClaw 覆盖 16 大功能分类、120+ 支持的操作：设备检查、通知和短信摘要、通话、系统设置、Wi-Fi 和蓝牙、截图和照片、屏幕读取、邮箱、日历、闹钟、本地笔记、地图、网页任务、工作流和快捷指令。'},
        'cmd1': {'en': 'Check my phone status', 'zh': '检查我的手机状态'},
        'cmd1_desc': {'en': 'Memory, storage, battery, network, and permission-risk report.', 'zh': '内存、存储、电池、网络和权限风险报告。'},
        'cmd2': {'en': "Summarize today's SMS", 'zh': '汇总今天的短信'},
        'cmd2_desc': {'en': 'Important items, pending replies, and risks grouped by contact.', 'zh': '按联系人分组的重要事项、待回复和风险。'},
        'cmd3': {'en': 'Set brightness to 60%', 'zh': '设置亮度为 60%'},
        'cmd3_desc': {'en': 'Supported Android setting changes with a clear result.', 'zh': '支持的 Android 设置变更，结果清晰。'},
        'cmd4': {'en': 'Take a screenshot', 'zh': '截图'},
        'cmd4_desc': {'en': 'Capture the current screen and summarize visible content.', 'zh': '捕获当前屏幕并摘要可见内容。'},
        'cmd5': {'en': 'What important notifications?', 'zh': '有什么重要通知？'},
        'cmd5_desc': {'en': 'Prioritize recent notifications from the phone.', 'zh': '优先显示手机上的最新通知。'},
        'cmd6': {'en': 'Check my email', 'zh': '检查我的邮箱'},
        'cmd6_desc': {'en': 'Read recent emails from configured IMAP/SMTP accounts.', 'zh': '读取已配置 IMAP/SMTP 账户的最新邮件。'},
        'cmd7': {'en': 'Where am I?', 'zh': '我在哪里？'},
        'cmd7_desc': {'en': 'Return location, coordinates, accuracy, source, and time.', 'zh': '返回位置、坐标、精度、来源和时间。'},
        'cmd8': {'en': 'Navigate by car', 'zh': '驾车导航'},
        'cmd8_desc': {'en': 'Open an installed map app and start navigation.', 'zh': '打开已安装的地图应用并开始导航。'},
    },

    # ═══════════════════════════════════════════
    # COMMUNITY PAGE
    # ═══════════════════════════════════════════
    'community': {
        'meta_title': {
            'en': 'FoneClaw Community - Join the Conversation',
            'zh': 'FoneClaw 社区 - 加入讨论',
        },
        'meta_desc': {
            'en': 'Join the FoneClaw community on Telegram, Discord, X, and more. Get updates, share feedback, and connect with other users.',
            'zh': '加入 FoneClaw 社区：Telegram、Discord、X 等。获取更新、分享反馈、与其他用户交流。',
        },
        'hero_title': {
            'en': 'Join the FoneClaw Community',
            'zh': '加入 FoneClaw 社区',
        },
        'hero_desc': {
            'en': 'Connect with other users, get early updates, and help shape the future of voice-controlled Android.',
            'zh': '加入 FoneClaw 社区，交流使用经验、了解产品更新，一起把 Android 语音控制做得更好。',
        },
    },

    # ═══════════════════════════════════════════
    # DOWNLOAD PAGE
    # ═══════════════════════════════════════════
    'download': {
        'meta_title': {
            'en': 'Download FoneClaw - AI Voice Agent for Android',
            'zh': '下载 FoneClaw - Android AI 语音助手',
        },
        'meta_desc': {
            'en': 'Download FoneClaw, the AI voice agent for Android. Control your phone entirely by voice — calls, texts, apps, and smart home. Free core features.',
            'zh': '下载 FoneClaw，Android AI 语音助手。完全通过语音控制手机——通话、短信、应用和智能家居。核心功能免费。',
        },
        'hero_title': {
            'en': 'Download FoneClaw',
            'zh': '下载 FoneClaw',
        },
        'hero_subtitle': {
            'en': 'Free for core features. No credit card required.',
            'zh': '核心功能可免费使用，无需付款。',
        },
        'product_desc': {
            'en': 'System-level AI agent for Android 9+. Voice control, cross-app automation, memory learning.',
            'zh': 'Android 9+ 系统级 AI 助手。语音控制、跨应用自动化，越用越懂你。',
        },
        'req_title': {
            'en': 'System Requirements',
            'zh': '系统要求',
        },
        'req_desc': {
            'en': 'Make sure your device meets these requirements.',
            'zh': '请确认您的设备满足以下要求。',
        },
        'faq_title': {
            'en': 'Frequently Asked Questions',
            'zh': '常见问题',
        },
        'faq_free_q': {
            'en': 'Is FoneClaw really free?',
            'zh': 'FoneClaw 真的免费吗？',
        },
        'faq_free_a': {
            'en': 'Yes. Core features are free. We may offer a Pro plan with advanced features later, but the core voice agent, basic automation, and system controls will always be free.',
            'zh': '是的，当前核心功能可免费使用。未来可能会推出高级功能或 Pro 计划，届时会明确说明价格和可用范围。',
        },
        'faq_phones_q': {
            'en': 'Does it work on all Android phones?',
            'zh': '支持所有 Android 手机吗？',
        },
        'faq_phones_a': {
            'en': 'FoneClaw requires Android 9 or higher with at least 3GB of RAM. It works on most modern Android devices including Samsung, Google Pixel, OnePlus, and Xiaomi phones.',
            'zh': 'FoneClaw 需要 Android 9 或更高版本，至少 3GB 内存。支持大多数现代 Android 设备，包括三星、Google Pixel、一加和小米手机。',
        },
        'faq_data_q': {
            'en': 'Is my data safe?',
            'zh': '我的数据安全吗？',
        },
        'faq_data_a': {
            'en': 'Yes. FoneClaw processes everything locally on your device. Your voice commands, contacts, and personal data never leave your phone unless you explicitly enable cloud sync.',
            'zh': '是的。FoneClaw 在您的设备上本地处理所有数据。除非您明确启用云同步，否则语音指令、联系人和个人数据不会离开您的手机。',
        },
        'req_android': {'en': 'Android 9.0 or higher', 'zh': 'Android 9.0 或更高版本'},
        'req_ram': {'en': '3GB RAM minimum', 'zh': '至少 3GB 内存'},
        'req_storage': {'en': '100MB storage space', 'zh': '100MB 存储空间'},
        'req_mic': {'en': 'Microphone permission', 'zh': '麦克风权限'},
        'req_accessibility': {'en': 'Accessibility Service access', 'zh': '无障碍服务权限'},
        'faq_available_q': {
            'en': 'When will it be available?',
            'zh': '什么时候可以下载？',
        },
        'faq_available_a': {
            'en': 'FoneClaw is available as an Android APK. Use the Download APK button above to get the latest available version.',
            'zh': 'FoneClaw 已提供 Android APK 下载。点击上方的"下载 APK"按钮获取最新版本。',
        },
    },
}


# Source-backed Traditional Chinese (Taiwan) translations.
# Keep TW copy separate so it can be rewritten for Taiwan usage rather than
# patched directly into generated /tw/*.html files.
try:
    from _tw_translations import TW_TRANSLATIONS
    for _page, _entries in TW_TRANSLATIONS.items():
        for _key, _text in _entries.items():
            TRANSLATIONS.setdefault(_page, {}).setdefault(_key, {})['tw'] = _text
except Exception:
    pass


def get_text(page, key, lang='en'):
    """Get translated text for a page/key/language."""
    return TRANSLATIONS.get(page, {}).get(key, {}).get(lang, TRANSLATIONS.get(page, {}).get(key, {}).get('en', key))


def generate_hreflang_tags(canonical_path, current_lang='en'):
    """Generate hreflang link tags for all language versions of a page."""
    tags = []
    for code, info in LANGUAGES.items():
        hreflang_code = info.get('hreflang', code)
        if info['dir']:
            href = f'https://www.foneclaw.ai/{info["dir"]}{canonical_path}'
        else:
            href = f'https://www.foneclaw.ai{canonical_path}'
        tags.append(f'<link rel="alternate" hreflang="{hreflang_code}" href="{href}">')
    # x-default points to English
    tags.append(f'<link rel="alternate" hreflang="x-default" href="https://www.foneclaw.ai{canonical_path}">')
    return '\n'.join(tags)


def generate_lang_switcher(current_lang='en'):
    """Generate language switcher HTML."""
    items = []
    for code, info in LANGUAGES.items():
        active = ' class="on"' if code == current_lang else ''
        if info['dir']:
            href = f'/{info["dir"]}/'
        else:
            href = '/'
        items.append(f'<a{active} href="{href}">{info["native"]}</a>')
    return '<div class="lang-switcher">' + ''.join(items) + '</div>'


def get_lang_dir(lang):
    """Get the directory prefix for a language. Returns '' for default (en)."""
    return LANGUAGES.get(lang, {}).get('dir', '')
