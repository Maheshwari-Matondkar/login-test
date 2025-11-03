import unittest
import HtmlTestRunner

suite = unittest.defaultTestLoader.discover('tests')
runner = HtmlTestRunner.HTMLTestRunner(
    output='reports',
    report_name='LoginTest',
    verbosity=2
)
runner.run(suite)