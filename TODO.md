# TODO - About Section Redesign

## Steps

1. [x] Remove the picture column from the About section in index.html
2. [x] Redesign About content into a full-width, balanced layout (bio + two info columns)
3. [x] Add supporting CSS for the new About layout in assets/css/style.css
4. [x] Remove "What I Do" highlights and replace with animated stats + tech stack marquee
5. [x] Switch About section to a clean, professional dark theme
6. [x] Highlight "React Native Developer" with a role badge
7. [x] Replace Personal Info / Quick Facts columns with info tiles + quick-fact chips
8. [x] Redesign Skills section with skill cards (icons, pills, animated progress bars) in dark theme
9. [x] Fully redesign Portfolio section with modern cards, dark filter bar, hover overlays, and updated lightbox
10. [x] Remove web projects and video links; keep only apps with proper alignment
11. [x] Display each project as a full-width row (image left, content right)
12. [x] Replace modal/page details with inline expandable details
13. [x] Fix All/Apps filter switching (simple show/hide preserving full-width rows)
14. [x] Replace Hitec Booking with Shagf (Fitness Coach Booking App) keeping same imagee
15. [x] Add multi-image slider support; add two images to Shagf with autoplay, arrows, and dots
16. [x] Adjust portfolio image sizing for 2000x1250 (16:10 aspect ratio)
17. [x] Remove the "App" tag chip from portfolio cards
18. [x] Change "View Details" button to "Expand" with expand icon
19. [x] Show project name on hover overlay instead of "Mobile App"
20. [x] Add "Shagf Trainer (Trainer App)" project below Shagf
21. [x] Add "Tallah Mobile App" project below the Shagf projects
22. [x] Update the SkillBot project to "Code Quiz (Skillbot)"
23. [x] Remove the Tap Rapid project
24. [x] Fix Expand button only working on the first project (attach handler to all buttons)
25. [x] Redesign the Services section to match the new dark theme
26. [x] Update contact info (phone +92 371 1449470, email mahmadhassan.c@gmail.com) across About, Resume, and contact form
27. [x] Remove repeated image (Code Quiz was using tallah.jpg; changed to skillbot.jpeg)
28. [x] Simplify About section into a clear layout (title + bio + 4 info cards)
29. [x] Revert the "Technologies I work with" label to its original style
30. [x] Fix mobile sizing of the tech marquee (smaller font/spacing so names aren't cut off)
31. [x] Remove the global `.about p` 100px font-size rule that was making the "Technologies I work with" label huge
32. [x] Remove contact info cards from About section
33. [x] Add a Contact section at the end of the page (info + form) with matching dark theme
34. [x] Make the contact info values bolder and brighter for easier reading
35. [x] Replace contact info icons with bolder filled boxicons and make icon boxes larger/prominent
36. [x] Add WhatsApp contact item and give each contact icon a distinct brand color
37. [x] Fix contact icon alignment and boldness
38. [x] Switch to standard bx boxicon classes (guaranteed to render) for contact icons
39. [x] Make the hero social icons (Facebook, Instagram, LinkedIn) bold, prominent, and visible
40. [x] Remove circles from hero social icons; use clean brand-colored icons aligned with text
41. [x] Center the hero social icons under the text on all screen sizes
42. [x] Make hero social icons responsive: centered on mobile, left-aligned under text on desktop
43. [x] Add WhatsApp icon to hero social links
44. [x] Add floating WhatsApp bubble fixed in bottom-right corner with pulse animation and tooltip
45. [x] Increase contrast of hero social icons (brighter colors, larger size, colored glow)
46. [x] Add subtle opacity (0.75) to hero social icons, restored to full on hover
47. [x] Make all hero social icons the same color (site accent blue), white on hover
48. [x] Remove the glow (drop-shadow) from hero social icons
49. [x] Verify the final result
50. [x] Move the Skills section to appear directly under the Portfolio (projects) section
51. [x] Simplify the Skills section - remove Advanced/Intermediate level labels
52. [x] Reduce the skills list to the essential React Native stack (no more 3-column groups)
53. [x] Update skills CSS for the simplified single-list responsive layout
54. [x] Add attractive tech icons (React Native, Expo, Firebase, TypeScript, etc.) to the skills list
55. [x] Add a "Built with" tech-stack icon strip (React Native, Expo, Firebase, TypeScript, JavaScript) to the Hero section
56. [x] Remove the tech icons from both the Skills section and the Hero section (reverted)
57. [x] Add custom mouse cursor (dot + smooth trailing ring) effect to the portfolio
58. [x] Simplify cursor into a single elegant glowing orb that follows the mouse
59. [x] Replace glow orb with a particle trail that matches the tech/developer vibe (blue & orange dots that fade out)
60. [x] Make trail single-color (blue) and much smoother/silkier for a satisfying scroll feel
61. [x] Replace dots with a smooth fading line trail (canvas) that fades with opacity
62. [x] Replace line trail with a subtle, minimal cursor aura (barely-visible glowing halo that smoothly follows the cursor)
63. [x] Tone down the aura further so it's barely perceptible (smaller + fainter)
64. [x] Replace the aura with a premium cursor: precise dot + a ring that lags softly behind (feels weighty/smooth)
65. [x] Simplify Contact section icons to a clean, minimal single-color style (blue squares, no brand colors)
66. [x] Remove the custom cursor dot + ring (revert to native browser cursor)
67. [x] Add native smooth scrolling for a silky, fluid page feel
68. [x] Audit full project and delete unused images, PDF, and portfolio-details.html (broken refs)
69. [x] Remove commented-out unused CSS image reference
70. [x] Fix slow page load: remove unused/blocking CDN resources (fancybox, lightbox2) and add defer to all local JS
71. [x] Full SEO + keyword optimization: title, description, keywords, Open Graph, Twitter, geo tags, canonical, JSON-LD schema
72. [x] Add keyword-rich on-page content (hero, about, portfolio, services)
73. [x] Add robots.txt and sitemap.xml
74. [x] Add "Tallah Admin" portfolio project (shop registration + admin approval + booking management dashboard)
75. [x] Add original brand tool icons (via simple-icons CDN) to each portfolio project card
76. [x] Fix broken tool icons: replace CDN (reactnative 404, openai 404) with locally-hosted colorized brand SVGs in assets/img/tools/
77. [x] Remove icon name labels so only the authentic brand logos show; fix black SVGs by injecting the correct brand fill color into each SVG
78. [x] Upgrade to authentic colorful brand logos using Devicon library (react, redux, firebase, tailwind, javascript) + official OpenAI mark, downloaded locally
79. [x] Simplify tool icons: remove background/border, make small (22px), right-align in card
80. [x] Add Play Store / App Store download links to each portfolio card (placeholder URLs to fill in)
        Yes
        no n
