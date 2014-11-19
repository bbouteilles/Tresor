# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Tresor
                                 A QGIS plugin
 Chasse au trésor (jeu pédagogique)
                             -------------------
        begin                : 2014-11-18
        copyright            : (C) 2014 by Bertrand Bouteilles
        email                : bertrand.bouteilles@ardeche.gouv.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Tresor class from file Tresor
    from tresor import Tresor
    return Tresor(iface)
