# coding=utf-8
import os
import argparse


# This class copy from
# https://stackoverflow.com/questions/23936145/python-argparse-help-message-disable-metavar-for-short-options#answer-23941599
class CustomFormatter(argparse.HelpFormatter):

    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append('%s' % option_string)
                parts[-1] += ' %s' % args_string
            return ', '.join(parts)


def _get_app_path(args):
    base_dir = os.path.abspath('.')
    app_name = args.app
    app_path = os.path.join(base_dir, app_name)
    if app_name not in os.listdir(base_dir):
        print('Error:There is no [{}] in [{}]'.format(app_name, base_dir))
        raise SystemExit
    if not os.path.isdir(app_path):
        print('app path [{}] is not directory.'.format(app_path))
        raise SystemExit
    if 'apps.py' not in os.listdir(app_path):
        print('[{}] not a Django app'.format(app_path))
        raise SystemExit
    return app_path


def _handle_add_parameter(args, app_path):
    if args.add not in ['forms', 'urls']:
        raise ValueError("add parameter must be on of ['forms', 'urls']")
    if args.add == 'forms':
        filepath = os.path.join(app_path, 'forms.py')
        if os.path.exists(filepath):
            print('{} existed!'.format(filepath))
        else:
            with open(filepath, 'w', encoding='utf-8')as fl:
                fl.write('from django import forms\n')
            print('{} created successfully.'.format(filepath))
    elif args.add == 'urls':
        filepath = os.path.join(app_path, 'urls.py')
        if os.path.exists(filepath):
            print('{} existed!'.format(filepath))
        else:
            urls_content = '''
from django.urls import path
from . import views

app_name = '{}'
urlpatterns = [
]
'''
            with open(filepath, 'w', encoding='utf-8')as fl:
                fl.write(urls_content.format(args.app).lstrip())
            print('{} created successfully.'.format(filepath))


def _handle_template(args, app_path):
    templates_dir = os.path.join(app_path, 'templates', args.app)
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
        print('{} created successfully.'.format(templates_dir))
    template_abs_path = os.path.join(templates_dir, args.template)
    if os.path.exists(template_abs_path):
        print('{} existed!'.format(template_abs_path))
    else:
        with open(template_abs_path, 'w', encoding='utf-8')as fl:
            pass
        print('{} created successfully.'.format(template_abs_path))


def _handle_static(args, app_path):
    static_dir = os.path.join(app_path, 'static', args.app)
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print('created {} successfully.'.format(static_dir))
    static_abs_path = os.path.join(static_dir, args.static)
    if os.path.exists(static_abs_path):
        print('{} existed!'.format(static_abs_path))
    else:
        '''为了让脚本适应一些平常可以使用到的情况，比如在 static 的
        目标文件夹下，我们可能再创建 css 和 js 文件夹以便更好管理这些
        静态文件。为此这里需要多加一个创建文件夹的代码。更具体的使用方式
        请看 README.md 文件
        '''
        tmp_dir = os.path.dirname(static_abs_path)
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
            print('{} created successfully.'.format(tmp_dir))
        with open(static_abs_path, 'w', encoding='utf-8')as fl:
            pass
        print('{} created successfully.'.format(static_abs_path))


def main():
    parser = argparse.ArgumentParser(
        description='Easily to create files when using django',
        epilog='You must cd BASE_DIR to run this script',
        formatter_class=CustomFormatter)
    parser.add_argument('--app',
                        required=True,
                        help='input the app name which django created')
    parser.add_argument(
        '-a', '--add', help="add file automatically, the value must be one of ['forms', 'urls']")
    parser.add_argument('-t', '--template', help='add templates html files')
    parser.add_argument('-s', '--static', help='add static files')
    args = parser.parse_args()

    app_path = _get_app_path(args)

    if args.add:
        _handle_add_parameter(args, app_path)

    if args.template:
        _handle_template(args, app_path)

    if args.static:
        _handle_static(args, app_path)

if __name__ == '__main__':
    main()
