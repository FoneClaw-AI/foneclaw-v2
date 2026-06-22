# FoneClaw Features — 16 Categories, 120+ Actions

FoneClaw supports 120+ voice-controlled phone actions organized into 16 categories. Each action is designed to work on any Android 9+ device without root access.

## Category Overview

| # | Category | Actions | Description |
|---|----------|---------|-------------|
| 1 | Phone Status | 9 | Battery, storage, network, permission risk reports |
| 2 | Notifications | 6 | Summarize and prioritize notifications by contact and time |
| 3 | SMS | 6 | Send, read, and summarize text messages |
| 4 | Calls | 3 | Make and manage phone calls |
| 5 | System Settings | 18 | Brightness, volume, Do Not Disturb, Wi-Fi, Bluetooth, airplane mode |
| 6 | Wi-Fi & Bluetooth | 12 | Scan networks, connect, pair devices, forget connections |
| 7 | Screenshots | 8 | Capture screen, analyze content, share screenshots |
| 8 | Screen Reading | 2 | Read and summarize visible screen content |
| 9 | Email | 10 | Read and compose emails from IMAP/SMTP accounts |
| 10 | Calendar | 6 | Create events, check schedule, set reminders |
| 11 | Alarms | 2 | Set and manage alarms |
| 12 | Notes | 9 | Create and manage local notes |
| 13 | Maps & Navigation | 8 | Search nearby places, get directions, share location |
| 14 | Web | 3 | Search the web, fill forms, browser automation |
| 15 | Workflows | 3 | Multi-step cross-app automation |
| 16 | App Interface | Quick | Open apps, interact with UI elements |

## Core Scenarios

### Daily Briefing
FoneClaw summarizes your SMS, notifications, and system information by contact and time. See what matters without opening every app.

### Phone Health
Get a single-voice-command report on battery, storage, network, and permission risks. No need to dig through Android settings.

### Passive Triggers
FoneClaw detects screenshots and photos in any app automatically and provides summaries. No context switching required.

## Command Examples

- "Check my phone status"
- "What are my important notifications?"
- "Read my latest SMS"
- "Call Mom"
- "Set brightness to 60%"
- "Connect to Office Wi-Fi"
- "Take a screenshot"
- "What's on my screen?"
- "Check my email"
- "What's on my calendar today?"
- "Set an alarm for 7 AM"
- "Create a note: buy groceries"
- "Navigate to the nearest gas station"
- "Search for nearby restaurants"
- "Send a WhatsApp message to John saying I'll be late"
- "Open Spotify and play my playlist"

## Permissions Model

FoneClaw organizes permissions by category. You only grant what you need:

- **Microphone** — Voice input for commands
- **Accessibility Service** — Phone control (reading screen, performing actions)
- **Notifications** — Summarizing notification content
- **Contacts** — Looking up contact names for calls/messages
- **SMS** — Reading and sending text messages
- **Calendar** — Managing events and reminders
- **Storage** — Accessing notes and screenshots

Each permission is requested explicitly. Sensitive actions (sending messages, making calls, changing settings) require your confirmation before execution.

## Technical Requirements

- Android 9.0 or higher
- 3 GB RAM minimum
- 100 MB storage
- Internet connection (for AI-powered features; some basic actions work offline)
- No root required
