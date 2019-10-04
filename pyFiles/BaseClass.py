
#===============================================================================#
# import internal dependencies                                                  #
#===============================================================================#

#===============================================================================#
# import external dependencies                                                  #
#===============================================================================#

#===============================================================================#
# BaseClass definition                                                          #
#===============================================================================#

class BaseClass:

    #===========================================================================#
    # constructor                                                               #
    #===========================================================================#

    def __init__( self, name, *args, **kwargs ):
        """
        use:
        instructions on how to perform basic construction for any class instance
        that inherits BaseClass.

        If single *arg provided, assumes it is a file name to a pickled
        dictionary. Loads all the items in the pickled dictionary as instance
        attributes.

        Adds any items in **kwargs as attributes as well.

        ========================================================================
        input:          type:           description:
        ========================================================================
        args:

        kwargs:

        ========================================================================
        output:         type:
        ========================================================================
        None            None
        """

    #===========================================================================#
    # public methods                                                            #
    #===========================================================================#

    #===========================================================================#
    # sudo-protected methods                                                    #
    #===========================================================================#

    #===========================================================================#
    # sudo-private methods                                                      #
    #===========================================================================#
