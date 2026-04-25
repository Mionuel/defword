import click

@click.command()
@click.option('-c', '--count', default=1, type=int, help='number of greetings')
def hello(count):
    click.echo(f"Hello World! {count}")
    
if __name__ == '__main__':
    hello() 
