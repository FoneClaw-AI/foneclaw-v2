# FoneClaw Supported Devices & Requirements

## System Requirements

| Requirement | Minimum |
|-------------|---------|
| Android version | 9.0 (Pie) or higher |
| RAM | 3 GB |
| Storage | 100 MB |
| Internet | Required for AI features; some basic actions work offline |
| Root | Not required |

## Supported Manufacturers

FoneClaw works on **any Android device** from any manufacturer. Tested and verified on:

| Manufacturer | Examples |
|-------------|----------|
| Samsung | Galaxy S series, Galaxy A series, Galaxy Z series |
| Xiaomi | Mi series, Redmi series, POCO series |
| Google | Pixel 4 and later |
| OnePlus | OnePlus 8 and later |
| Motorola | Moto G series, Edge series |
| OPPO | Find series, Reno series |
| Realme | GT series, Number series |
| Vivo | X series, V series |
| Sony | Xperia series |
| LG | Velvet, Wing (legacy) |
| Nokia | G series, X series |
| Nothing | Phone (1), Phone (2) |

## What "Android 9+" Means

Android 9 (Pie) was released in August 2018. Any Android phone purchased from 2018 onward should run FoneClaw. This covers the vast majority of active Android devices worldwide.

To check your Android version: Settings → About Phone → Android Version.

## Permissions Explained

FoneClaw requests permissions organized by function:

| Permission | Why FoneClaw Needs It | Can You Revoke? |
|-----------|----------------------|-----------------|
| Microphone | Voice input for commands | Yes — FoneClaw won't work without it |
| Accessibility Service | Reading screen content, performing taps and swipes | Yes — core phone control won't work |
| Notifications | Summarizing notification content | Yes — notification features disabled |
| Contacts | Looking up contact names for calls/messages | Yes — contact-based commands disabled |
| SMS | Reading and sending text messages | Yes — SMS features disabled |
| Calendar | Managing events and reminders | Yes — calendar features disabled |
| Storage | Accessing notes and screenshots | Yes — note/screenshot features disabled |

**Important**: FoneClaw never grants itself permissions. You approve each one individually. You can revoke any permission at any time through Android Settings → Apps → FoneClaw → Permissions.

## Accessibility Service

FoneClaw uses Android's Accessibility Service to interact with your phone's interface. This is the same technology used by screen readers (TalkBack) and other accessibility tools.

What it allows FoneClaw to do:
- Read text displayed on screen
- Identify buttons, text fields, and other UI elements
- Perform taps, swipes, and other interactions
- Navigate between apps and screens

What it does NOT allow:
- Access to other apps' private data
- Bypassing security locks
- Installing apps without your consent
- Sending messages without your confirmation

## Frequently Asked Questions

**Q: Does FoneClaw work on tablets?**
A: FoneClaw is designed for phones. It may work on Android tablets but is not officially supported.

**Q: Does FoneClaw work on custom ROMs (LineageOS, /e/OS, etc.)?**
A: FoneClaw should work on custom ROMs based on Android 9+, but some features may behave differently depending on the ROM's Accessibility Service implementation.

**Q: Does FoneClaw work on Android Go edition?**
A: Android Go devices typically have 1-2 GB RAM, which is below FoneClaw's 3 GB minimum. Performance may be limited.

**Q: Does FoneClaw work on Huawei devices without Google Play Services?**
A: FoneClaw does not require Google Play Services for core functionality, but some features may be affected. Huawei devices with Android 9+ should work.
