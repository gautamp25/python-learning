import click
import errno
import os
import pandas as pd
# https://blog.piinalpin.com/2020/12/sql-generator/
# sql_generator.py --generate cc.xlsx --outputdir D:/DataStructureAndAlgorithm/basics/daily-scripts
@click.command()
@click.option('--generate', '-g', help='Change TEXT to generate excel file into SQL insert')
@click.option('--outputdir', '-o', help='Change TEXT to create directory output file')
def main(generate, outputdir):
	try:
		# Validate generate file can not be None
		if generate is None:
			raise TypeError

		# Check if outputdir is not None
		if outputdir != None:
			try:
				# Create a directory
				os.makedirs(outputdir)
				# outputdir = f"{outputdir}"
				outputdir = "{}/".format(outputdir)
			except OSError as exc:
				# If directory is exists use this directory
				if exc.errno == errno.EEXIST:
					# outputdir = f"{outputdir}/"
					outputdir = "{}/".format(outputdir)
		file = pd.ExcelFile(generate)
		for sheet_name in file.sheet_names:
			data = file.parse(sheet_name)
			# filename = f"{outputdir}{sheet_name}.sql"
			# click.echo(f"### {filename}:")
			filename = "{}{}.sql".format(outputdir, sheet_name)
		    # click.echo("### {}:".format(filename))
			# click.echo(f"### {filename}:")
			with open(filename, "w",encoding="utf-8") as write_file:
				for i, _ in data.iterrows():
					field_names = ", ".join(list(data.columns))
					rows = [str(data[column][i]) for column in data.columns]
					# print(rows[0].isnumeric())
					row_values =  "'" + "', '".join(rows) + "'"
					# click.echo(f"INSERT INTO {sheet_name} ({field_names}) VALUES ({row_values});")
					# click.echo("INSERT INTO {} ({}) VALUES ({});".format(sheet_name, field_names, row_values))
					write_file.write("INSERT INTO {} ({}) VALUES ({});\n".format(sheet_name, field_names, row_values))
					# write_file.write(
					# 	f"INSERT INTO {sheet_name} ({field_names}) VALUES ({row_values});\n"
					# )
	except TypeError as e:
		click.echo("Error: Unknown generate file! Type -h for help.")

if __name__ == "__main__":
    main()
