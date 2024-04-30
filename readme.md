Changes made to initial models.py in readdb
    Renamed dept_name to name in the Department model for clarity.
    Renamed dept_name to department in the Student, Course, and Instructor models for consistency.
    Renamed prereq to prerequisite_course in the Prerequisite model for clarity.
    Updated related names in the Prerequisite model to prerequisites and dependent_courses.
    Removed null=True from the Prerequisite model's fields since prerequisites should always be specified.
    Updated the __str__ method in the Prerequisite model to provide a clearer representation.


    F3
    Course Sections
        I have professor name, year, semester
        course name, sections, semester