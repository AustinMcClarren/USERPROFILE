import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL statements
cursor = db.cursor()

# Create the survey_responses table
create_table_query = """
CREATE TABLE survey_responses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  age_range VARCHAR(20),
  gender VARCHAR(20),
  household_size VARCHAR(20),
  num_rooms VARCHAR(20),
  num_people_per_room VARCHAR(20),
  education_level VARCHAR(50),
  annual_income VARCHAR(50),
  ethnic_background VARCHAR(50),
  primary_language VARCHAR(50),
  disabilities VARCHAR(5),
  employment_status VARCHAR(50),
  government_assistance VARCHAR(5),
  years_in_current_home VARCHAR(20),
  housing_type VARCHAR(50),
  homeowner_or_renter VARCHAR(20),
  repairs_or_renovations VARCHAR(5),
  interest_in_energy_efficiency VARCHAR(20),
  awareness_of_renewable_energy_programs VARCHAR(5),
  concerns_or_barriers VARCHAR(100),
  home_condition VARCHAR(20),
  square_footage VARCHAR(20),
  num_bedrooms VARCHAR(20),
  energy_efficient_appliances VARCHAR(5),
  interest_in_renewable_energy VARCHAR(20),
  financial_assistance_for_home_improvements VARCHAR(5),
  home_remodeling_completed VARCHAR(5),
  remodeling_projects_completed VARCHAR(100),
  planning_home_remodeling VARCHAR(5),
  factors_influencing_remodeling_decision VARCHAR(100),
  awareness_of_local_programs VARCHAR(5),
  interest_in_installing_renewable_energy VARCHAR(20),
  motivations_for_adopting_renewable_energy VARCHAR(100),
  familiarity_with_renewable_energy_options VARCHAR(5),
  concerns_or_barriers_to_renewable_energy VARCHAR(100),
  interest_in_home_energy_audit VARCHAR(5),
  energy_efficiency_upgrades VARCHAR(100),
  interest_in_energy_saving_workshops VARCHAR(20),
  interest_in_financial_assistance_programs VARCHAR(20),
  challenges_in_obtaining_financing VARCHAR(5),
  guidance_for_applying_for_loans VARCHAR(5),
  concerns_about_home_safety_and_security VARCHAR(5),
  interest_in_home_security_measures VARCHAR(20),
  guidance_on_home_safety_topics VARCHAR(5),
  awareness_of_community_programs VARCHAR(5),
  helpful_information_or_resources VARCHAR(100),
  challenges_in_accessing_information VARCHAR(5)
)
"""

cursor.execute(create_table_query)

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()

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
