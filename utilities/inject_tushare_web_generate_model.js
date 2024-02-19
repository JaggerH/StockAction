function generateArrayFromTableColumn($table) {
    let arrayResult = [];

    $table.find('tr').each(function(index) {
        // Skip the header row
        if (index === 0) return;

        const $cells = $(this).find('td');
        if ($cells.length > 0) {
            const firstColumnText = $cells.eq(0).text();
            arrayResult.push(firstColumnText);
        }
    });

    return JSON.stringify(arrayResult);
}

generateArrayFromTableColumn($($('table')[1]))
