## Description

- (Description), Fixes # (issue)

## Type of change

Please delete the unrelated option:

- Bug fix (fixes an issue without introducing new features)
- Enhancement (improves existing functionality without breaking it)
- New feature (adds new functionality)
- Breaking change (fix or feature that would cause existing functionality to not work as expected)
- Need Documentation update

## Checklist:

- [ ] Make sure it can be exported properly by doing `sh run -e`, the file will be exported to the `/dist` folder.
- [ ] Ensure streamlit can run properly. `sh run -s`
- [ ] There is a change in requirements.txt
- [ ] There are changes to the `run` and `active` file scripts
- [ ] There is a change in `.env.example`
- [ ] There is a change in `.gitignore`
- [ ] Adding a new folder
