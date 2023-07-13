from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Retrieve the form data
        age_range = request.form["age_range"]
        gender = request.form["gender"]
        household_size = request.form["household_size"]
        # Retrieve other form fields in a similar manner

        # Insert the survey response into the database
        sql = """
        INSERT INTO survey_responses (
          age_range, gender, household_size, num_rooms, num_people_per_room, education_level,
          annual_income, ethnic_background, primary_language, disabilities, employment_status,
          government_assistance, years_in_current_home, housing_type, homeowner_or_renter,
          repairs_or_renovations, interest_in_energy_efficiency, awareness_of_renewable_energy_programs,
          concerns_or_barriers, home_condition, square_footage, num_bedrooms,
          energy_efficient_appliances, interest_in_renewable_energy, financial_assistance_for_home_improvements,
          home_remodeling_completed, remodeling_projects_completed, planning_home_remodeling,
          factors_influencing_remodeling_decision, awareness_of_local_programs,
          interest_in_installing_renewable_energy, motivations_for_adopting_renewable_energy,
          familiarity_with_renewable_energy_options, concerns_or_barriers_to_renewable_energy,
          interest_in_home_energy_audit, energy_efficiency_upgrades, interest_in_energy_saving_workshops,
          interest_in_financial_assistance_programs, challenges_in_obtaining_financing,
          guidance_for_applying_for_loans, concerns_about_home_safety_and_security,
          interest_in_home_security_measures, guidance_on_home_safety_topics,
          awareness_of_community_programs, helpful_information_or_resources,
          challenges_in_accessing_information
        ) VALUES (
          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """
        values = (
          age_range, gender, household_size, num_rooms, num_people_per_room, education_level,
          annual_income, ethnic_background, primary_language, disabilities, employment_status,
          government_assistance, years_in_current_home, housing_type, homeowner_or_renter,
          repairs_or_renovations, interest_in_energy_efficiency, awareness_of_renewable_energy_programs,
          concerns_or_barriers, home_condition, square_footage, num_bedrooms,
          energy_efficient_appliances, interest_in_renewable_energy, financial_assistance_for_home_improvements,
          home_remodeling_completed, remodeling_projects_completed, planning_home_remodeling,
          factors_influencing_remodeling_decision, awareness_of_local_programs,
          interest_in_installing_renewable_energy, motivations_for_adopting_renewable_energy,
          familiarity_with_renewable_energy_options, concerns_or_barriers_to_renewable_energy,
          interest_in_home_energy_audit, energy_efficiency_upgrades, interest_in_energy_saving_workshops,
          interest_in_financial_assistance_programs, challenges_in_obtaining_financing,
          guidance_for_applying_for_loans, concerns_about_home_safety_and_security,
          interest_in_home_security_measures, guidance_on_home_safety_topics,
          awareness_of_community_programs, helpful_information_or_resources,
          challenges_in_accessing_information
        )
        cursor.execute(sql, values)
        db.commit()

        return "Thank you for your response!"

    return render_template("survey.html")


if __name__ == "__main__":
    app.run()
