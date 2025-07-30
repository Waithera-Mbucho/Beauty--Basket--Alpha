# Beauty--Basket--Alpha

Beauty Basket Alpha: Dermatology-Backed Skincare Optimizer

Beauty Basket Alpha  is a quantitative skincare portfolio optimizer designed to help users invest in high-performing products tailored to clinical markers of skin health.  

Inspired by financial modeling and backed by dermatology board standards, it uses scientifically defined skin quality factors  to deliver maximum Glow Score under a user-defined budget.

---

## Why This Project?
In my late teens, I struggled with chronic acne—an experience that caused me emotional distress and a deep sense of insecurity. I didn’t have access to dermatologists, and coming from a background with limited financial resources, I couldn’t afford to experiment with expensive skincare routines or play trial-and-error with trending products.

What made it worse wasn’t just the skin issues, but the **lack of guidance** on what actually worked. I was stuck between TikTok hype and drugstore disappointment.

That frustration became the seed of **Beauty Basket Alpha**.

I wanted to build something that **I wish I had** back then: a smart, data-driven way to invest in skincare products that deliver real results without wasting time or money.


I use the four emergent skin quality categories defined by international dermatologists as the foundation for our Glow Score:

- **Skin Tone Evenness**
- **Surface Evenness**
- **Firmness**
- **Skin Glow**

---
## 🌍 Market Context: Why Skincare Optimization Matters

The **skincare industry** is one of the fastest-growing consumer markets in the world, making Beauty Basket Alpha highly relevant and timely:

- As of 2024, the global skincare market was valued between USD 115.65 billion :contentReference[oaicite:1]{index=1} and USD 142.49 billion :contentReference[oaicite:2]{index=2}, depending on source.

- Forecasts show strong growth to USD 151.3 billion by 2025 :contentReference[oaicite:3]{index=3}, and to as high as **USD 194–196 billion by 2030** :contentReference[oaicite:4]{index=4}.

- Some projections go further—estimating the global skincare market reaching USD 432 billion by 2035, with a CAGR of 6–8% :contentReference[oaicite:5]{index=5}.

This massive growth is driven by:
- Increasing consumer awareness of skin health as self-care
- A shift toward science-backed, efficacy-based products
- The rising power of social media and trend virality, especially among Gen Z consumers who often rely on influencer-led skincare routines :contentReference[oaicite:7]{index=7}

Beauty Basket Alpha enters this space by combining dermatology-backed factors with quant-based optimization—ensuring users don’t waste time, money, or fall prey to trending but ineffective products.


## 🔬 Glow Score Formula (v2.0)

```python
glow_score = (
  0.3 * tone_evenness_score +
  0.25 * surface_evenness_score +
  0.25 * firmness_score +
  0.2 * glow_radiance_score
)
