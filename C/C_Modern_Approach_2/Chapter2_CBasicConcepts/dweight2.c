/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* dweight2.c (Chapter 2, page 23) */
/* Computes the dimensional weight of a
   box from input provided by the user */

#include <stdio.h>

int dweight2(void)
{
  int height, length, width, volume, weight;

  printf("Enter height of box: ");
  scanf_s("%d", &height);
  printf("Enter length of box: ");
  scanf_s("%d", &length);
  printf("Enter width of box: ");
  scanf_s("%d", &width);
  volume = height * length * width;
  weight = (volume + 165) / 166;

  printf("Volume (cubic inches): %d\n", volume);
  printf("Dimensional weight (pounds): %d\n", weight);

  return 0;
}
