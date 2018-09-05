# github-skills
> Get the "skills" or percentage of language usage for a github user.

## Using the library
> Just import it and run like this:

    from github_skills import get_skills


    my_skills = get_skills('someuser123_hey')

    # [{"language": "C++", "percentage": 23.56}, ...]

> the method `get_skills` returns a list of dictionaries, with the language
> and the percentage.

## Using the CLI
> Here is how you use it in your terminal:

    $ github-skills someuser2313_hey
    language    percentage
    ----------  ------------
    TypeScript  6.25%
    Java        6.25%
    C#          6.25%
    JavaScript  68.75%
    Python      6.25%
    Shell       6.25%    

> Usage: `github-skills <username>`


## Installing
> To install the library, clone down the repository and run:

    python setup.py install

> OR run:

    pip install github-skills
