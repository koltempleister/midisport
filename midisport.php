<?php

/**
* klein script om patchbay info aan te maken voor midisport 8x8
* in config array wordt beschreven met welke out poorten (1-8) elke in poort is verbonden
*/

/*
binary reversed to correct binary, converted to hex, padded with zero and uppercased
*/
function output($binstring){
	return strtoupper(
			str_pad(
				dechex(
					bindec(
						strrev($binstring)
						)
					),
				2, '0' , STR_PAD_LEFT
				)
			);
}


$config = [
   '1' => [2],
   '2' => [2,4],
   '3' => [3,4,5],
   '4' =>[7],
   '5' =>[2,3,4],
   '6' =>[4,5,6],
   '7' =>[8],
   '8' =>[1,8],
];

$all_ports = range(1,8);

foreach ( $config as $in_port) {
    $str1 = '';
    $str2 = '';

    foreach($all_ports as $port) {
        if($port < 5) $str1 .= in_array($port, $in_port) ? 1 : 0;
        else $str2 .= in_array($port, $in_port) ? 1 : 0;
    }

    $binout[] = strrev($str1) . ' ' . strrev($str2);
    $out[] = output($str1) . ' ' . output($str2);
}

//echo to control binary codes
//echo implode(' ' , $binout) . PHP_EOL;

echo sprintf(
		'F0 %s %s %s %s F7',
		'00 01 05', //m-audio sysex id
		'7F 00 00 04 00 01', //device id
		'01', //patch number
		implode(' ',$out) //port config
	);
