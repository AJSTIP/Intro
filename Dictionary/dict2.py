test_scores = {'Kayla': [56, 78, 90],
               'John': [45, 67, 89],
               'Alice': [78, 88, 92],
               }

employee = {
    'Name': 'Kevin',
    'ID' : '12345',
    'Department' : 'Sales',
    'Salary' : 50000,
    'Bonus' : 5000,
    'Performance' : 'Excellent',
    'Skills' : ['Communication', 'Negotiation', 'Customer Service'],
    'Projects' : ['Project A', 'Project B', 'Project C'],
    'Location' : 'New York',
    'Experience' : 5,
    'Education' : {
        'Degree': 'Bachelor of Science',
        'Major': 'Business Administration',
        'University': 'XYZ University',
        'Graduation Year': 2018
    },
}

print(test_scores['Kayla'])
print(employee.get('Name'), employee.get('Skills'))