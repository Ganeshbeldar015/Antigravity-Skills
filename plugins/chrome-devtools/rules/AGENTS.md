# Browser & Performance Engineering Rules

When developing or debugging web frontend applications:
1. Never leave unhandled promise rejections or console errors in production builds.
2. Always specify aspect ratios or explicit dimensions for media elements to prevent layout shifts (CLS).
3. Do not perform synchronous layout reads and writes in tight loops (prevent layout thrashing).
4. Defer non-critical third-party scripts and analytics to avoid blocking First Contentful Paint.
5. Ensure all images are served in modern formats (AVIF / WebP) with responsive `srcset` definitions.
