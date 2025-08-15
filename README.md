# About This Project

This project is part of the CloudSec initiative, providing a RESTful API for managing policy data in a PostgreSQLdatabase. It allows for creating, retrieving, updating, and deleting policies with various attributes such as tenant, subject, action, and more.

CloudSec (cloudsecpy on PyPI) is a library and toolkit for formally analyzing security policies in cloud and API systems using Python. It has a modular and extensible architecture allowing it to support multiple backends; currently, z3 and cvc5 are supported, but more backends will be supported in the future. The CloudSec project takes influence from a number of related projects, such as the Z3 Firewall Checker.

### Related Projects

- Main CloudSec Repository: https://github.com/applyfmsec/cloudsec
  This API is a component of the larger CloudSec Project.

### Description

This Policy Database API is a core component of the CloudSec security management system. It provides the backend infrastructure for managing securit  policies across cloud environments, enabling organizations to define, store,and enforce access control policies.

## Features

- RESTful API endpoints for policy management
- PostgreSQL database integration
- Docker support for easy deployment
- CRUD Operations: Create, read, update, delete polcies
- Pagination
- Advanced search
- Field Filtering: Include/exclude specific fields in responses


## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker

### Using Docker Compose
Docker Compose is the easiest way to run the entire application stack. It automatically handles container dependencies, networking and data persistence.
 
1. Clone the repository
   git clone https://github.com/joshuatallas/CloudSec.git
   cd Cloudsec

2. Use the provided 'docker-compose.yml' file
   This project includes a pre-configured 'docker-compose.yml' file that sets up both the PostgreSQL database and the API.

3. Start the entire stack using
   docker-compose up -d 

### How to use the API using curl commands
Basic Search: curl "http://localhost:5000/policies/search?tenant=TACC&decision=allow"

Field Filtering: curl "http://localhost:5000/policies/search?fields=policy_name,tenant,decision&tenant=TACC" 

Pagination: curl "http://localhost:5000/policies/search?limit=3&offset=0"

### Importing data from a JSON file

1. Create a JSON file and name it "create_policy.json" for example.
2. Copy this into the JSON file you just created and enter new data in the fields.

 {
    "policy_name": "Admin Access Policy",
    "tenant": "TACC",
    "subject": "admin_user",
    "policy_description": "Full administrative access to all resources",
    "action": "POST",
    "created_by": "system_admin",
    "policy_type": "access",
    "policy_schema": "v9",
    "resource": "api/data",
    "decision": "allow",
    "owner": "dev_team",
    "project": "administration"
  }

3. Import/create new policy data using curl command:
curl -X POST http://localhost:5000/policies -H "Content-Type: application/json" -d @create_policy.json
 

## Contact

Github: joshuatallas https://github.com/joshuatallas
LinkedIn: www.linkedin.com/in/joshua-tallas

## Acknowledgements

*This work has been funded by grants from the National Science Foundation, including the Leadership-Class Computing Facility and Tapis (OAC 1931439).
