import re

# Function to validate phone number
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Function to validate email
def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email)

# Collect user inputs
name = input("Enter your name: ").strip()
job_role = input("Enter your job role: ").strip()
objective = input("Enter your career objective or professional summary: ").strip()

# Validate phone number
while True:
    phone_no = input("Enter your phone number (10 digits): ").strip()
    if validate_phone(phone_no):
        break
    print("Invalid phone number. Please enter a valid 10-digit phone number.")

# Validate email
while True:
    email = input("Enter your email (must be a Gmail address): ").strip()
    if validate_email(email):
        break
    print("Invalid email. Please enter a valid Gmail address (e.g., abc@gmail.com).")

linkedin = input("Enter your LinkedIn profile URL: ").strip()
github = input("Enter your GitHub profile URL: ").strip()
college_name = input("Enter your college name: ").strip()
branch = input("Enter your branch: ").strip()
percentage = input("Enter your percentage: ").strip()

# Technical Skills input
technical_skills = [input(f"Enter technical skill {i+1}: ").strip() for i in range(5) if input(f"Do you have technical skill {i+1}? (yes/no): ").strip().lower() == "yes"]

# Soft Skills input
soft_skills = [input(f"Enter soft skill {i+1}: ").strip() for i in range(5) if input(f"Do you have soft skill {i+1}? (yes/no): ").strip().lower() == "yes"]

# Languages Known input with proficiency
languages_known = [input(f"Enter language {i+1} and proficiency (e.g., English - Fluent): ").strip() for i in range(3)]

# Achievements input
achievements = [input(f"Enter achievement {i+1}: ").strip() for i in range(5) if input(f"Do you have achievement {i+1}? (yes/no): ").strip().lower() == "yes"]

# Hobbies and Interests input
hobbies = [input(f"Enter hobby or interest {i+1}: ").strip() for i in range(3)]

# Projects input
projects = []
for i in range(2):  # Example: Two projects
    title = input(f"Enter project {i+1} title: ").strip()
    role = input(f"Enter project {i+1} role: ").strip()
    description = input(f"Enter project {i+1} description: ").strip()
    projects.append((title, role, description))

# Experience input
has_experience = input("Do you have any prior experience? (yes/no): ").strip().lower()
if has_experience == "yes":
    company_name = input("Enter company name for experience: ").strip()
    experience_role = input("Enter your role at the company: ").strip()
    experience_description = input("Enter your job description at the company: ").strip()
else:
    company_name = None
    experience_role = None
    experience_description = None

# Certification input
certifications = []
if input("Do you have any certifications? (yes/no): ").strip().lower() == "yes":
    for i in range(5):  # Example: Up to 5 certifications
        title = input(f"Enter certification {i+1} title: ").strip()
        company_name_cert = input(f"Enter certification {i+1} company name: ").strip()
        certifications.append((title, company_name_cert))

# HTML content for the resume
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{name} - Resume</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background: #f7f9fc;
      color: #333;
    }}
    .header {{
      background-color: #2d3e50;
      color: white;
      padding: 30px 20px;
      text-align: center;
    }}
    .header h1 {{
      margin: 0;
      font-size: 36px;
    }}
    .header p {{
      margin: 5px 0;
      font-size: 18px;
    }}

    .container {{
      display: grid;
      grid-template-columns: 30% 70%;
      gap: 20px;
      padding: 20px;
      max-width: 1200px;
      margin: auto;
    }}

    .left, .right {{
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}

    h2 {{
      border-bottom: 2px solid #ddd;
      padding-bottom: 5px;
      margin-bottom: 15px;
      color: #2d3e50;
    }}

    .section p, li {{
      margin: 10px 0;
      line-height: 1.5;
    }}

    ul {{
      padding-left: 20px;
    }}

    .skills li {{
      background-color: #e0e0e0;
      display: inline-block;
      margin: 5px 5px 0 0;
      padding: 5px 12px;
      border-radius: 20px;
    }}

    .project-item {{
      margin-bottom: 20px;
    }}

    .project-item strong {{
      display: block;
      font-size: 16px;
      color: #444;
    }}

    .certifications li {{
      margin-bottom: 8px;
    }}

    .contact-info p {{
      margin: 8px 0;
    }}
  </style>
</head>
<body>

  <div class="header">
    <h1>{name}</h1>
    <p>{job_role}</p>
  </div>

  <div class="container">
    <!-- Left Sidebar -->
    <div class="left">
      <h2>Contact</h2>
      <div class="contact-info">
        <p><strong>Phone:</strong> {phone_no}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>LinkedIn:</strong> <a href="{linkedin}" target="_blank">Visit LinkedIn</a></p>
        <p><strong>GitHub:</strong> <a href="{github}" target="_blank">Visit GitHub</a></p>
      </div>

      <h2>Technical Skills</h2>
      <ul class="skills">
        {''.join([f'<li>{skill}</li>' for skill in technical_skills])}
      </ul>

      <h2>Soft Skills</h2>
      <ul class="skills">
        {''.join([f'<li>{skill}</li>' for skill in soft_skills])}
      </ul>

      <h2>Languages Known</h2>
      <ul class="skills">
        {''.join([f'<li>{language}</li>' for language in languages_known])}
      </ul>

      <h2>Hobbies and Interests</h2>
      <ul>
        {''.join([f'<li>{hobby}</li>' for hobby in hobbies])}
      </ul>
    </div>

    <!-- Right Content -->
    <div class="right">
      <div class="section">
        <h2>Objective</h2>
        <p>{objective}</p>
      </div>

      <div class="section">
        <h2>Projects</h2>
        {''.join([f'<div class="project-item"><strong>{project[0]} ({project[1]})</strong><p>{project[2]}</p></div>' for project in projects])}
      </div>

      <div class="section">
        <h2>Achievements</h2>
        <ul>
          {''.join([f'<li>{achievement}</li>' for achievement in achievements])}
        </ul>
      </div>

      {"<div class='section'><h2>Experience</h2><p><strong>Company:</strong> " + company_name + "</p><p><strong>Role:</strong> " + experience_role + "</p><p><strong>Description:</strong> " + experience_description + "</p></div>" if has_experience == "yes" else ""}
      
      <div class="section">
        <h2>Certifications</h2>
        <ul class="certifications">
          {''.join([f'<li><strong>{cert[0]}</strong> – {cert[1]}</li>' for cert in certifications])}
        </ul>
      </div>
    </div>
  </div>

</body>
</html>
"""

# Save to an HTML file
with open("resume.html", "w") as f:
    f.write(html_content)

print("HTML Resume saved as resume.html")