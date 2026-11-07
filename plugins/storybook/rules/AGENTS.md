# Storybook Behavioral Guidelines

When `storybook` is active:
1. Always query Storybook components (`get-stories`) before generating new UI elements to prevent duplicate implementations.
2. Adhere to documented prop schemas and variant configurations when composing views with existing design system primitives.
3. Keep all newly created components accompanied by standard `.stories.tsx` files.
4. Maintain accessibility annotations and controls across component story definitions.
