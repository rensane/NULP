gpa = 4.6
is_active_in_student_council = True
has_volunteer_experience = False

if gpa >= 4.5 and is_active_in_student_council:
    scholarship_type = "full"
elif gpa >= 4.0 or has_volunteer_experience:
    scholarship_type = "partial"
elif not (gpa >= 4.5 and is_active_in_student_council) and not (gpa >= 4.0 or has_volunteer_experience):
    scholarship_type = "no"

print(f"Тип стипендії: {scholarship_type}")