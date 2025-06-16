# 🧠 PostHog Demo: User Attribution & Cohort Dashboard (Portfolio Project)

This project demonstrates how to use **PostHog**, **BigQuery-style SQL**, and data analytics techniques to analyze user behavior, marketing attribution, and retention cohorts.

It’s built using the **PostHog demo project**, with sample data and SQL queries that can be extended to real projects.

---

## 🔧 Tools Used

- [PostHog](https://posthog.com/) – Product analytics platform
- SQL (BigQuery-style)
- HTML + JavaScript (for event tracking example)
- Google Sheets or BigQuery (for analysis using exported data)

---

## 📈 What You'll Learn

- How to track and analyze user behavior events
- How to calculate retention cohorts using SQL
- How to identify traffic sources via attribution analysis
- How to build simple dashboards for user insights

---

## 🚀 Getting Started

### Step 1: Explore PostHog Demo Data
1. Sign up at [PostHog](https://app.posthog.com)
2. Click your profile picture > “Try the demo project”
3. Explore dashboards, events, and funnels

### Step 2: Export Demo Data
1. Go to **Events** tab
2. Filter or keep default data
3. Click “Export → CSV”
4. Save the file in `demo_data/posthog_export.csv`

---

## 🧪 Example SQL Queries

### 📊 Attribution by Source

```sql
SELECT 
  properties.$set_utm_source AS source,
  COUNT(*) AS signups
FROM `posthog_export`
WHERE event = 'signup'
GROUP BY source
ORDER BY signups DESC;
