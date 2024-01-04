import resumai.resume as resume


def test_reading_resume():
    parsed_resume = resume.read_resume("tests/resources/example_resume.toml")

    skills = {
        "Technologies": ["Python", "Rust"],
        "Competencies": ["Communication", "Teamwork", "Leadership"],
    }
    degree = resume.Degree(
        "B.S. Computer Science", "University of California, Santa Cruz", 2021, 3.5
    )
    job = resume.Job(
        "Google",
        "Software Engineer",
        "2021-01-01",
        "2022-01-01",
        ["I wrote code.", "I suffered."],
    )
    contact = resume.ContactInfo(
        "Shane",
        "Stephenson",
        "443-889-4517",
        "stephenson.shane.a@gmail.com",
        "linkedin.com/in/shane-stephenson-",
        "github.com/oatish",
        "oatbread.com",
    )
    expected_resume = resume.Resume(contact, skills, [degree], "A cool cat.", [job])
    assert parsed_resume == expected_resume
