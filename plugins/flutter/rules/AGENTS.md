# Flutter Behavioral Guidelines

When `flutter` is active:
1. Ensure all widget builds maintain clean separation between layout, business logic (BLoC, Riverpod, Provider), and service calls.
2. Structure responsive layouts using `LayoutBuilder`, `MediaQuery`, and adaptive scaffolds.
3. Keep widget trees shallow by decomposing complex sections into reusable dedicated widgets.
4. Run integration tests (`flutter test`) and verify zero analysis issues before shipping.
