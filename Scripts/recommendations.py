def generate_recommendations_from_analysis():
    """
    Generate business recommendations based on churn analysis, segmentation, and model interpretation.
    Returns a list of actionable recommendations.
    """

    recommendations = []

    # 1. High churn in early tenure
    recommendations.append(
        "🎯 Target customers in their first year (0–12 months) with onboarding support and loyalty incentives."
    )

    # 2. High churn among high-paying, month-to-month customers
    recommendations.append(
        "💰 Offer long-term contract upgrades and exclusive perks to high-value customers on month-to-month plans."
    )

    # 3. Fiber optic users show high churn
    recommendations.append(
        "📞 Bundle tech support and online security services with fiber optic internet plans to reduce churn."
    )

    # 4. Paperless billing and electronic check users are more likely to churn
    recommendations.append(
        "🧾 Encourage stable payment methods like credit card auto-pay and send reminders to paperless billing users."
    )

    # 5. Use predictive model to flag at-risk customers
    recommendations.append(
        "🧠 Integrate churn prediction scores into CRM to trigger personalized retention workflows for at-risk customers."
    )

    # 6. Estimate revenue impact
    recommendations.append(
        "📈 Reducing churn by 10% among high-value customers could save thousands in monthly revenue."
    )

    return recommendations


def print_recommendations():
    """Print recommendations to console."""
    recs = generate_recommendations_from_analysis()
    print("\n📌 Business Recommendations:")
    for rec in recs:
        print("-", rec)


def estimate_impact(df, churn_reduction_rate=0.1):
    """Estimate revenue impact of reducing churn."""
    avg_monthly_charge = df['MonthlyCharges'].mean()
    churned_customers = df[df['Churn'] == 1].shape[0]
    retained_customers = churned_customers * churn_reduction_rate
    estimated_savings = retained_customers * avg_monthly_charge
    print(f"💰 Estimated Monthly Revenue Saved: ${estimated_savings:.2f}")