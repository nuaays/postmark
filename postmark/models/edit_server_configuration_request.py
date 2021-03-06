# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EditServerConfigurationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, color=None, raw_email_enabled=None, delivery_hook_url=None, smtp_api_activated=None, inbound_hook_url=None, bounce_hook_url=None, open_hook_url=None, post_first_open_only=None, track_opens=None, track_links=None, inbound_domain=None, inbound_spam_threshold=None):
        """
        EditServerConfigurationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'color': 'str',
            'raw_email_enabled': 'bool',
            'delivery_hook_url': 'str',
            'smtp_api_activated': 'bool',
            'inbound_hook_url': 'str',
            'bounce_hook_url': 'str',
            'open_hook_url': 'str',
            'post_first_open_only': 'bool',
            'track_opens': 'bool',
            'track_links': 'str',
            'inbound_domain': 'str',
            'inbound_spam_threshold': 'int'
        }

        self.attribute_map = {
            'name': 'Name',
            'color': 'Color',
            'raw_email_enabled': 'RawEmailEnabled',
            'delivery_hook_url': 'DeliveryHookUrl',
            'smtp_api_activated': 'SmtpApiActivated',
            'inbound_hook_url': 'InboundHookUrl',
            'bounce_hook_url': 'BounceHookUrl',
            'open_hook_url': 'OpenHookUrl',
            'post_first_open_only': 'PostFirstOpenOnly',
            'track_opens': 'TrackOpens',
            'track_links': 'TrackLinks',
            'inbound_domain': 'InboundDomain',
            'inbound_spam_threshold': 'InboundSpamThreshold'
        }

        self._name = None
        self._color = None
        self._raw_email_enabled = None
        self._delivery_hook_url = None
        self._smtp_api_activated = None
        self._inbound_hook_url = None
        self._bounce_hook_url = None
        self._open_hook_url = None
        self._post_first_open_only = None
        self._track_opens = None
        self._track_links = None
        self._inbound_domain = None
        self._inbound_spam_threshold = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if name is not None:
          self.name = name
        if color is not None:
          self.color = color
        if raw_email_enabled is not None:
          self.raw_email_enabled = raw_email_enabled
        if delivery_hook_url is not None:
          self.delivery_hook_url = delivery_hook_url
        if smtp_api_activated is not None:
          self.smtp_api_activated = smtp_api_activated
        if inbound_hook_url is not None:
          self.inbound_hook_url = inbound_hook_url
        if bounce_hook_url is not None:
          self.bounce_hook_url = bounce_hook_url
        if open_hook_url is not None:
          self.open_hook_url = open_hook_url
        if post_first_open_only is not None:
          self.post_first_open_only = post_first_open_only
        if track_opens is not None:
          self.track_opens = track_opens
        if track_links is not None:
          self.track_links = track_links
        if inbound_domain is not None:
          self.inbound_domain = inbound_domain
        if inbound_spam_threshold is not None:
          self.inbound_spam_threshold = inbound_spam_threshold

    @property
    def name(self):
        """
        Gets the name of this EditServerConfigurationRequest.

        :return: The name of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EditServerConfigurationRequest.

        :param name: The name of this EditServerConfigurationRequest.
        :type: str
        """

        self._name = name

    @property
    def color(self):
        """
        Gets the color of this EditServerConfigurationRequest.

        :return: The color of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this EditServerConfigurationRequest.

        :param color: The color of this EditServerConfigurationRequest.
        :type: str
        """
        allowed_values = ["purple", "blue", "turqoise", "green", "red", "yellow", "grey"]
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def raw_email_enabled(self):
        """
        Gets the raw_email_enabled of this EditServerConfigurationRequest.

        :return: The raw_email_enabled of this EditServerConfigurationRequest.
        :rtype: bool
        """
        return self._raw_email_enabled

    @raw_email_enabled.setter
    def raw_email_enabled(self, raw_email_enabled):
        """
        Sets the raw_email_enabled of this EditServerConfigurationRequest.

        :param raw_email_enabled: The raw_email_enabled of this EditServerConfigurationRequest.
        :type: bool
        """

        self._raw_email_enabled = raw_email_enabled

    @property
    def delivery_hook_url(self):
        """
        Gets the delivery_hook_url of this EditServerConfigurationRequest.

        :return: The delivery_hook_url of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._delivery_hook_url

    @delivery_hook_url.setter
    def delivery_hook_url(self, delivery_hook_url):
        """
        Sets the delivery_hook_url of this EditServerConfigurationRequest.

        :param delivery_hook_url: The delivery_hook_url of this EditServerConfigurationRequest.
        :type: str
        """

        self._delivery_hook_url = delivery_hook_url

    @property
    def smtp_api_activated(self):
        """
        Gets the smtp_api_activated of this EditServerConfigurationRequest.

        :return: The smtp_api_activated of this EditServerConfigurationRequest.
        :rtype: bool
        """
        return self._smtp_api_activated

    @smtp_api_activated.setter
    def smtp_api_activated(self, smtp_api_activated):
        """
        Sets the smtp_api_activated of this EditServerConfigurationRequest.

        :param smtp_api_activated: The smtp_api_activated of this EditServerConfigurationRequest.
        :type: bool
        """

        self._smtp_api_activated = smtp_api_activated

    @property
    def inbound_hook_url(self):
        """
        Gets the inbound_hook_url of this EditServerConfigurationRequest.

        :return: The inbound_hook_url of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._inbound_hook_url

    @inbound_hook_url.setter
    def inbound_hook_url(self, inbound_hook_url):
        """
        Sets the inbound_hook_url of this EditServerConfigurationRequest.

        :param inbound_hook_url: The inbound_hook_url of this EditServerConfigurationRequest.
        :type: str
        """

        self._inbound_hook_url = inbound_hook_url

    @property
    def bounce_hook_url(self):
        """
        Gets the bounce_hook_url of this EditServerConfigurationRequest.

        :return: The bounce_hook_url of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._bounce_hook_url

    @bounce_hook_url.setter
    def bounce_hook_url(self, bounce_hook_url):
        """
        Sets the bounce_hook_url of this EditServerConfigurationRequest.

        :param bounce_hook_url: The bounce_hook_url of this EditServerConfigurationRequest.
        :type: str
        """

        self._bounce_hook_url = bounce_hook_url

    @property
    def open_hook_url(self):
        """
        Gets the open_hook_url of this EditServerConfigurationRequest.

        :return: The open_hook_url of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._open_hook_url

    @open_hook_url.setter
    def open_hook_url(self, open_hook_url):
        """
        Sets the open_hook_url of this EditServerConfigurationRequest.

        :param open_hook_url: The open_hook_url of this EditServerConfigurationRequest.
        :type: str
        """

        self._open_hook_url = open_hook_url

    @property
    def post_first_open_only(self):
        """
        Gets the post_first_open_only of this EditServerConfigurationRequest.

        :return: The post_first_open_only of this EditServerConfigurationRequest.
        :rtype: bool
        """
        return self._post_first_open_only

    @post_first_open_only.setter
    def post_first_open_only(self, post_first_open_only):
        """
        Sets the post_first_open_only of this EditServerConfigurationRequest.

        :param post_first_open_only: The post_first_open_only of this EditServerConfigurationRequest.
        :type: bool
        """

        self._post_first_open_only = post_first_open_only

    @property
    def track_opens(self):
        """
        Gets the track_opens of this EditServerConfigurationRequest.

        :return: The track_opens of this EditServerConfigurationRequest.
        :rtype: bool
        """
        return self._track_opens

    @track_opens.setter
    def track_opens(self, track_opens):
        """
        Sets the track_opens of this EditServerConfigurationRequest.

        :param track_opens: The track_opens of this EditServerConfigurationRequest.
        :type: bool
        """

        self._track_opens = track_opens

    @property
    def track_links(self):
        """
        Gets the track_links of this EditServerConfigurationRequest.

        :return: The track_links of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._track_links

    @track_links.setter
    def track_links(self, track_links):
        """
        Sets the track_links of this EditServerConfigurationRequest.

        :param track_links: The track_links of this EditServerConfigurationRequest.
        :type: str
        """
        allowed_values = ["None", "HtmlAndText", "HtmlOnly", "TextOnly"]
        if track_links not in allowed_values:
            raise ValueError(
                "Invalid value for `track_links` ({0}), must be one of {1}"
                .format(track_links, allowed_values)
            )

        self._track_links = track_links

    @property
    def inbound_domain(self):
        """
        Gets the inbound_domain of this EditServerConfigurationRequest.

        :return: The inbound_domain of this EditServerConfigurationRequest.
        :rtype: str
        """
        return self._inbound_domain

    @inbound_domain.setter
    def inbound_domain(self, inbound_domain):
        """
        Sets the inbound_domain of this EditServerConfigurationRequest.

        :param inbound_domain: The inbound_domain of this EditServerConfigurationRequest.
        :type: str
        """

        self._inbound_domain = inbound_domain

    @property
    def inbound_spam_threshold(self):
        """
        Gets the inbound_spam_threshold of this EditServerConfigurationRequest.

        :return: The inbound_spam_threshold of this EditServerConfigurationRequest.
        :rtype: int
        """
        return self._inbound_spam_threshold

    @inbound_spam_threshold.setter
    def inbound_spam_threshold(self, inbound_spam_threshold):
        """
        Sets the inbound_spam_threshold of this EditServerConfigurationRequest.

        :param inbound_spam_threshold: The inbound_spam_threshold of this EditServerConfigurationRequest.
        :type: int
        """

        self._inbound_spam_threshold = inbound_spam_threshold

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EditServerConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
