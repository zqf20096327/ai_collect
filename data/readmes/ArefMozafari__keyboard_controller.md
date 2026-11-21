# keyboard_controller

iOS-style interactive keyboard dismiss for Flutter, on iOS **and Android**: swipe the chat down
and the keyboard follows your finger. Plus a chat list that stays put while the keyboard moves,
a composer that rides the keyboard, and AI chat behaviours. It is the Flutter counterpart of
react-native-keyboard-controller, and goes beyond `keyboardDismissBehavior: onDrag`, which only
starts a dismiss animation.

| iOS: AI chat, pinned prompt, swipe to dismiss | Android: messenger, swipe to dismiss |
| --- | --- |
| ![The sent prompt stays at the top while the answer streams, then the keyboard is swiped down with the input bar riding on it](https://raw.githubusercontent.com/ArefMozafari/keyboard_controller/main/media/ios_ai_chat.gif) | ![The keyboard follows the finger down with the input bar on top, hides, and opens again](https://raw.githubusercontent.com/ArefMozafari/keyboard_controller/main/media/android_messenger.gif) |

```sh
flutter pub add keyboard_controller
```

## Features

- **Interactive dismiss.** Drag the message list down and the keyboard follows the finger once
  it reaches the keyboard's top edge. Let go low and it hides; let go high and it springs back.
  It uses public platform APIs only: UIKit's own interactive dismiss on iOS, and inset animation
  control on Android.
- **A list that stays put.** The newest message sits right above the input bar. When the
  keyboard opens, closes or is dragged, the list moves with it the way you choose. Messages
  arriving while you read history never move what you are reading.
- **A composer that rides the keyboard**, including while it is dragged, and pushes the list up
  as it grows to several lines.
- **Four lift behaviours**, named after the apps that use them:
  - `always`: Telegram, WhatsApp
  - `whenAtEnd`: ChatGPT
  - `persistent`: Claude
  - `never`: Perplexity
- **AI chat behaviours.**
  - The list follows an answer as it streams in.
  - `pinToTop` moves a sent prompt to the top of the screen while its answer grows below it.
  - `isAtEnd` drives a jump-to-latest button.
- **Keyboard state** as listenables: height, target height, progress (0 to 1) and phase.

## Usage

Put one `KeyboardScope` above the navigator, then use `KeyboardChatView` in a `Scaffold` that
does not resize for the keyboard:

```dart
MaterialApp(
  builder: (context, child) => KeyboardScope(child: child!),
  home: const ChatScreen(),
);

Scaffold(
  resizeToAvoidBottomInset: false,
  body: KeyboardChatView(
    controller: chatController, // a ChatScrollController
    itemCount: messages.length,
    itemKey: (index) => messages[index].id, // index 0 is the newest message
    itemBuilder: (context, index) => MessageBubble(messages[index]),
    composer: const MessageComposer(),
    liftBehavior: KeyboardLiftBehavior.whenAtEnd,
  ),
);
```

For an AI chat, insert the prompt and its answer placeholder, then pin the prompt:

```dart
setState(() {
  messages.insert(0, prompt);
  messages.insert(0, answer);
});
chatController.pinToTop(prompt.id);
```

`KeyboardChatView` asserts in debug builds when an ancestor already removed the keyboard inset,
which usually means `resizeToAvoidBottomInset` was left on.

Lower-level pieces for custom layouts:
- `KeyboardScope.of(context)` for the keyboard state.
- `KeyboardStickyView`: a child that rides the keyboard.
- `KeyboardDismissRegion`: interactive dismiss for any area.
- `KeyboardHoldScrollPhysics`: keeps your own scrollable still while the keyboard is dragged.

```dart
KeyboardDismissRegion(
  child: ListView(
    physics: KeyboardHoldScrollPhysics(keyboard: KeyboardScope.of(context)),
    children: messages,
  ),
);
```

## Platform support

| Platform | Minimum | Interactive dismiss |
| --- | --- | --- |
| iOS | 15 | Yes |
| Android | API 24 | API 30 and later; below that, dragging the list dismisses the keyboard |
| Other | Flutter 3.29 | No; keyboard state comes from `MediaQuery` insets |

Without native keyboard events (Android below API 30, web, desktop), `phase` and `targetHeight`
settle shortly after the inset stops changing, instead of at the start of the animation.

## Known limits

- Floating and undocked iPad keyboards are not tracked.
- An edited message in the older part of the history that changes height can still shift the
  messages above it.
- Deleting a message, or changing its key, moves the messages above it by that message's
  height; keep `itemKey` stable.
- Use one `KeyboardScope` per app; a second scope takes over the native channel from the first.

The example app in `example/` has a messenger screen and an AI chat screen with a simulated
streaming answer.
