from __future__ import absolute_import

import enviro


def test_parse():
    content = """
    ENV_VAR1=var1_value
    ENV_VAR2=var2_value
    #NO_ENV_VAR3=var3_value
    """

    d = enviro.parse(content)
    expected = {'ENV_VAR1': 'var1_value',
                'ENV_VAR2': 'var2_value'}
    assert d == expected


def test_update_no_force():
    env = {'ENV_VAR1': 'var1_value',
           'ENV_VAR2': 'var2_value'}

    d = {'ENV_VAR1': 'new_value',
         'ENV_VAR2': 'var3_value'}

    expected = env.copy()
    expected['ENV_VAR2'] = 'var2_value'

    enviro.updateenv(env, d)

    assert env == expected


def test_update_force():
    env = {'ENV_VAR1': 'var1_value',
           'ENV_VAR2': 'var2_value'}

    d = {'ENV_VAR1': 'new_value',
         'ENV_VAR2': 'var3_value'}

    expected = d.copy()
    expected['ENV_VAR3'] = 'var3_value'

    enviro.updateenv(env, d, force=True)

    assert env == d
