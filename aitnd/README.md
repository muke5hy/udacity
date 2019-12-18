# AI in Trading NanoDegree (AITND)
This repository contains code for Udacity's [AI in Trading NanoDegree](https://www.udacity.com/course/nd880).
## Repository File Structure
    .
    ├── project/             # Code for projects in the classroom
    ├── quiz/                # Code for quizzes in the classroom
    ├── helper.py            # A helper file shared across projects and quizzes
    ├── requierments.txt     # Common packages used for projects and quizzes
    └── tests.py             # Common test functions for unit testing student code in projects and quizzes
## No Data
We don't have a licence to redistribute the data to you. We're working on alternatives to this problem.


### To download data from workspace

```
import shutil
import errno 
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(os.path.join(os.getcwd(), '..', '..', 'data'), zipf)
zipf.close()

```

http 'https://bdmutualfund.paytmmoney.com/mf/v1/mf-scheme/transaction-meta/karvy?transactionTypeTag=N&schemeCode=STD2&amcCode=BARSPN&karvyTransactionIdentifier=D'

http 'https://bdmutualfund.paytmmoney.com/mf/v1/mf-scheme/transaction-meta?transactionTypeTag=N&schemeCode=STD2&amcCode=BARSPN&karvyTransactionIdentifier=D'EP-MF-UTIMF-K-201119-104135

