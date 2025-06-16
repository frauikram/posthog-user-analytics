SELECT
  COALESCE(utm_source, 'unknown') AS source,
  COUNT(DISTINCT user_id) AS signups
FROM 'demo_data/posthog_export.csv'
WHERE event = 'user_signed_up'
GROUP BY source
ORDER BY signups DESC;
